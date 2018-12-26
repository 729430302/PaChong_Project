import requests,threading
import lxml.etree
from bs4 import BeautifulSoup
import re
import html
from urllib import request
import time
import os
os.makedirs('G:/PaChong/A8', exist_ok=True)
'''
1、先获取html源码方法stream
2、获取资源连接，并用连接获取源码
3、获取图片url，或者资源url
4、通过图片连接下载图片，或通过url下载资源
5、增加多线程
'''
j = 0
for i in range(1, 24):
    print(i)
    url = 'http://www.xiaohuar.com/s-7-'
    url = url + str(i) + '.html'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    res = requests.get(url, headers=header)
    response = res.text

    soup = BeautifulSoup(response, 'html.parser', from_encoding='gbk')
    # /d/file/20151120/small1b4135f03c5993d6b23603b566ada12e1448006559.jpg
    imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))
    # print(imgs)
    for img in imgs:
        img = img['src']
        # /d/file/20151120/small1b4135f03c5993d6b23603b566ada12e1448006559.jpg
        img = img.replace('small', '')      #去掉字符串中small字符
        # /d/file/20151120/1b4135f03c5993d6b23603b566ada12e1448006559.jpg
        img = img[:49]      # 截取第49个字符之前所有字符
        img = img + '.jpg'
        url = "http://www.xiaohuar.com%s" % img
        req = request.Request(url=url, headers=header)
        # 获得了我们的图片信息
        data = request.urlopen(req).read()
        # 保存图片
        j = j + 1
        with open('G:\PaChong\A8\%s.jpg' % str(j), 'wb') as f:
            f.write(data)
