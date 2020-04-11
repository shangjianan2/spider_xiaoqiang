# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re
import os
from perType import Type

url = "http://m.123xiaoqiang.in/"

req = requests.get(url)
print type(req.content.decode('utf-8'))
soup1 = BeautifulSoup(req.content.decode('utf-8'), "lxml")
str1 = soup1.currentTag.encode("utf-8")
with open('1.txt', 'w') as f:
    f.write(str1)


novelClasses = soup1.find("ul", {"id":"tag_ul"}).find_all('li')

s = requests.session()
s.keep_alive = False
for i in novelClasses:
    className = str(i.find('a').text.encode('gbk'))
    print(className)
    # className = str(i.find('a').text.encode('utf-8'))
    pathToStore = './novel/' + className
    if(os.path.exists(pathToStore) == False):
        os.makedirs(pathToStore)
    t = Type('http://m.123xiaoqiang.in' + i.find('a')['href'], s)
    lll = t.getList()
    with open('./' + className + '.txt', 'a') as f:
        for item in lll:
            f.write(item + '\r\n')

    