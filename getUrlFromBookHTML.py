# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re

class getUrlFromBookHTML:
    def __init__(self, url):
        self.url = url
    
    def doget(self):
        req = requests.get(self.url)
        soup = BeautifulSoup(req.text)
        lianjie = soup.find('div', {'id':'chapterlist'}).find_all('p')

        resList = []
        for s in lianjie:
            sss = s.find('a')['href']
            if(sss == "#bottom"):
                continue
            resList.append('http://m.123xiaoqiang.in' + sss)
        
        return resList

if __name__ == '__main__':
    url = "http://m.123xiaoqiang.in/book/6571.html"
    test = getUrlFromBookHTML(url)
    resList = test.doget()
    for s in resList:
        print s
