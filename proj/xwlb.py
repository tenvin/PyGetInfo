# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
from datetime import *

s = requests.Session()

def yesterday():
    return (date.today()+timedelta(-1)).strftime('%Y%m%d')

def go():
    URL_Base = 'http://tv.cctv.com/lm/xwlb/day/'+yesterday()+'.shtml'
    r = s.get(URL_Base)
    content = BeautifulSoup(r.content)

    for i in content:
        for newsitem in i.find_all('li'):
            print newsitem.string
            r = s.get(newsitem.a.get('href'))
            detail = BeautifulSoup(r.content)
            text = detail.find(class_= 'mbd')
            print text.get_text()
if __name__ == '__main__':
    go()
