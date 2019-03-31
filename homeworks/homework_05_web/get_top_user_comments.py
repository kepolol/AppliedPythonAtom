import sys
import requests
from bs4 import BeautifulSoup
import re
from multiprocessing.dummy import Pool
from functools import partial
import pandas as pd


# Ваши импорты
def link_parser(our_dict, link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")
    for i in soup.findAll("a", attrs={"class": ["user-info user-info_inline"]}):
        if our_dict.get((i['data-user-login'], link)) is None:
            # Такое значение ключа на случай, если один и тот же комментатор будет в разных постах.
            our_dict[(i['data-user-login'], link)] = 1
        else:
            our_dict[(i['data-user-login'], link)] += 1
    return our_dict


if __name__ == '__main__':
    filename = 'top_user_comments.csv'
    links = sys.argv[1:4]

    # Ваш код
    our_dict = {}
    func = partial(link_parser, our_dict)
    pool = Pool(len(links))
    pool.map(func, links)
    df = pd.DataFrame([[i[1], i[0], our_dict[i]] for i in our_dict])
    df.sort_values(by=[df.columns[2], df.columns[1]], ascending=False, inplace=True)
    df.to_csv('top_user_comments.csv', index=False, header=False)
