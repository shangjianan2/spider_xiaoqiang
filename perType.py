# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re
import os
import time

class Type:
    def __init__(self, url, session):
        self.baseUrl = self.parseUrl(url)
        self.session = session
        self.info = self.getPageInfo(url)
    
    def getList(self):
        info1 = self.info
        resList = []

        for i in range(1, info1+1):
            bs = self.turnPage(i)
            allNovel = bs.find_all('div', {'class':'hot_sale'})
            for item in allNovel:
                sss = item.find('a')['href']
                newUrl_novel = 'http://m.123xiaoqiang.in' + sss
                resList.append(newUrl_novel)
        
        return resList


    def getPageInfo(self, url):
        req = self.session.get(url)
        infos = BeautifulSoup(req.content.decode('utf-8'), "lxml").find('input', {'class':'page_txt'})['value']
        infoArray = infos.split('/')
        return int(infoArray[1])

    def turnPage(self, yema):
        newUrl = self.baseUrl + str(yema) + '.html'
        req = self.session.get(newUrl)
        time.sleep(2)
        return BeautifulSoup(req.content.decode('utf-8'), "lxml")

    def parseUrl(self, url):
        sArrays = url.split('/')
        baseUrl = ''
        for i in range(len(sArrays) - 1):
            baseUrl += sArrays[i]
            baseUrl += '/'
        return baseUrl

if __name__ == '__main__':
    s = requests.session()
    s.keep_alive = False
    t = Type('http://m.123xiaoqiang.in/tag/0/50/2.html', s)
    lll = t.getList()