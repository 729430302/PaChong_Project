#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
# import os
# os.makedirs('G:/PaChong/1', exist_ok=True)
# 初始url
# first_url = "http://www.xiaohuar.com/p-6-1.html"
x = 0
start_url = 'http://www.xiaohuar.com/p-6-'
for i in range(28, 46):
    i = str(i)
    first_url = start_url + i + '.html'
    # 发送一个请求
    header = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                }
    # 包装一个请求
    req = request.Request(url=first_url, headers=header)

    response = request.urlopen(req)
    # 获取返回的html
    html = response.read()
    # 我们要提取所有我们需要的img
    soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')

    # 获取所有的img
    imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))
    print(imgs)

    for img in imgs:
        # 创建一个请求
        # "/d/file/20170707/f7ca636f73937e33836e765b7261f036.jpg"
        img = img['src']
        img = img.replace('small', '')      #去掉字符串中small字符
        img = img[:49]      # 截取第49个字符之前所有字符
        img = img + '.jpg'
        url = "http://www.xiaohuar.com%s" % img
        req = request.Request(url=url, headers=header)
        # 获得了我们的图片信息
        data = request.urlopen(req).read()
        # 保存图片
        x = x + 1
        with open('G:\PaChong\A11\%s.jpg' % str(x), 'wb') as f:
            f.write(data)
