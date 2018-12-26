#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time

# 原地址 = 'http://www.tu11.com/qingchunmeinvxiezhen/list_4_1.html'

IP = '111.230.254.195:8118'
UA = ''
proxies = {'http': IP}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}

for i in range(1, 2):
    url = 'http://www.tu11.com/qingchunmeinvxiezhen/list_4_'
    url = url + str(i) + '.html'

    res = requests.get(url=url, headers=header, verify=False,
                       # proxies=proxies
                       )
    htmls1 = res.content
    # print(htmls1)

    soup = BeautifulSoup(htmls1, 'html.parser', from_encoding='gbk')
    # html1 = soup.find_all('a', href=re.compile(r'/qingchunmeinvxiezhen/\d+/\d+\.html'))  # 获取所有的html
    html1 = soup.find_all('a', class_='leibie')         # 获取所有的html
    # print(html1)

    '''========================================分隔符=============================================='''
    # jpgs = soup.find_all('img', class_='img-responsive picheng')   # 获取所有的jpg
    # for img in jpgs:
    #     url = img['src']
    #     name = img['alt']
    #     res = requests.get(url=url, headers=header)
    #     html2 = res.content
    #     with open('G:\PaChong\A10\ %s.jpg' % name, 'wb') as f:
    #         f.write(html2)
    '''========================================分隔符=============================================='''

    for html in html1:
        html_url = 'http://www.tu11.com' + html['href']
        # print(html_url)
        # http://www.tu11.com/qingchunmeinvxiezhen/2018/
        str_num1 = url[46:-5]  # 拿到14220
        # print(str_num)
        str_num2 = url[:-10]  # 拿到http://www.tu11.com/qingchunmeinvxiezhen/2018/
        res = requests.get(url=url, headers=header)
        html2 = res.content
        # print(html2)
        soup = BeautifulSoup(html2, 'html.parser', from_encoding='gbk')
        imgs2 = soup.find_all('img', src=re.compile(r'/picture/\d+/\w+/\d\.jpg'))  # 获取所有的img
        # imgs2 = soup.find_all('a', class_='nry')
        # print(imgs2)
        for img in imgs2:
            img_url = img['src']
            # print(img_url)
            res = requests.get(url=img_url, headers=header)
            img = res.content
            # print(img)
            with open('G:\PaChong\A11\ %s.jpg' % time.time(), 'wb') as f:
                f.write(img)


        # '14220_2.html'
        soup = BeautifulSoup(html2, 'html.parser', from_encoding='gbk')
        html3 = soup.find_all('a', href=re.compile(str_num1 + r'_\d\.html'))  # 获取所有的img
        # print(html3)

        if html3:
            url_list = []
            for img1 in html3:
                try:
                    img_url1 = img1['href']
                    img_url1 = str_num2 + img_url1
                    url_list.append(img_url1)
                    print(url_list[0])
                except:
                    print('无图片')


            res = requests.get(url=url_list[0], headers=header)
            img = res.content

            soup = BeautifulSoup(img, 'html.parser', from_encoding='gbk')
            imgs3 = soup.find_all('img', src=re.compile(r'/picture/\d+/\w+/\d\.jpg'))  # 获取所有的img

            for img in imgs3:
                url3 = img['src']
                # print(img_url)
                res = requests.get(url=url3, headers=header)
                img = res.content
                # print(img)
                with open('G:\PaChong\A11\ %s.jpg' % time.time(), 'wb') as f:
                    f.write(img)

#获取地址
#获取图片
#下载图片
#判读地址是否有
    # 获取图片
    #下载图片