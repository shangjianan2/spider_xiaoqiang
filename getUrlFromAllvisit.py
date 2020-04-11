# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re

class getUrlFromAllvisit:
    def __init__(self, url):
        self.url = url

    def doget(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text, 'lxml')
        lianjie = soup.select('div[id="alist"] > div[id="alistbox"] > div[class="info"] > div[class="title"] > h2 > a')
        
        resList = []
        for s in lianjie:
            resList.append(s['href'])
        
        return resList

if __name__ == '__main__':
    url = "http://www.123xiaoqiang.me/modules/article/toplist.php?sort=allvisit&page=1"
    test = getUrlFromAllvisit(url)
    resList = test.doget()
    for s in resList:
        print(s)
