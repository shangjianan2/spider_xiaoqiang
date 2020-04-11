# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re
import io
import os
class getnovel:
    def __init__(self, url, path):
        self.url = url
        self.path = path
    
    def doget(self):
        session = requests.session()
        session.keep_alive = False
        soup = self.sessionToBs(session, self.url)
        title = soup.find('title')
        strTitle = title.contents[0].encode('utf-8')
        pages_urls = self.get_pages_urls(soup)
        cur_path = self.path + '/'
        if(os.path.exists(cur_path) == False):
            os.makedirs(cur_path)

        print(cur_path + strTitle)
        with open(cur_path + strTitle + '.txt', 'a') as f:
            for url in pages_urls:
                soup = self.sessionToBs(session, url)
                try:
                    chaptercontents = soup.find('div', {'id':'chaptercontent'}).contents
                    for c in chaptercontents:
                        c_str = c.encode('utf-8')
                        if(c_str != '<br/>'):
                            f.write(c_str)
                        else:
                            f.write('\r\n')
                
                except Exception as e:
                    print('do not has chaptercontent')
                finally:
                    pass
    
    def get_pages_urls(self, bs):
        resList = []
        resList.append(self.url)
        try:            
            lll = bs.find('div', {'class':'chapterPages'}).find_all('a')        

            sArray = self.url.split('/')
            basePath = ''
            for j in range(len(sArray) - 1):
                basePath += sArray[j]
                basePath += '/'

            resList = []
            for l in lll:
                newPath = basePath + l['href']
                resList.append(newPath)
                        
        finally:
            return resList
    
    def sessionToBs(self, session, url):
        req = session.get(url)
        soup = BeautifulSoup(req.content)
        return soup

        

if __name__ == '__main__':
    # 输入小说阅读页面的url
    url = 'http://m.123xiaoqiang.in/16_16139/1020484.html'
    a = getnovel(url = url, path = '')
    a.doget()
