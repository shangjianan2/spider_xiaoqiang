# -*- coding: utf-8 -*-
import urllib3
from bs4 import BeautifulSoup
import requests
import re
from getnovel import getnovel
from getUrlFromBookHTML import getUrlFromBookHTML
import os
import time

files = os.listdir('./type')

for fff in files:
    fList = os.listdir('./novel')
    flag = False
    for fL in fList:
        print(fL)
        if(fL + '.txt' == fff):
            print(fff + ' is ignored')
            flag = True
            break
    if(flag == True):
        continue
    print('begin downloading ' + fff)
    pathToStore = './novel/' + fff.split('.')[0]
    try:
        with open('./type/' + fff, 'r') as f:
            for l in f.readlines():
                if(l != ""):
                    l = l.replace("\n", "")
                    l = l.replace("\r", "")

                    jiList = []
                    try:
                        jiList = getUrlFromBookHTML(l + 'all.html').doget()
                    except Exception as e:
                        print('getUrlFromBookHTML has error')
                        continue

                    for url in jiList:
                        try:
                            a = getnovel(url = url, path = pathToStore)
                            a.doget()
                        except Exception as e:
                            print('doget has error')
                        time.sleep(5)
    except Exception as e:
        print('somewhere has error')
