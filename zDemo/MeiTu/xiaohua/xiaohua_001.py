import requests,threading
import lxml.etree
from bs4 import BeautifulSoup
import re
import html
from urllib import request
import time
import os
os.makedirs('G:/PaChong/A6', exist_ok=True)
'''
1、先获取html源码方法stream
2、获取资源连接，并用连接获取源码
3、获取图片url，或者资源url
4、通过图片连接下载图片，或通过url下载资源
5、增加多线程
'''
j = 0
for i in range(1, 99, 8):
    url = 'http://www.xiaohuar.com/e/wap/data_pic.php'
    data = {'offset': i}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    res = requests.get(url, data, headers=header)
    response = res.text
    response = eval(response)
    html1 = response['html']
    # print(html1)
    html2 = html.unescape(html1)
    # print(html2)
    soup = BeautifulSoup(html2, 'html.parser', from_encoding='gbk')
    # http://www.xiaohuar.com/d/file/20151120/fd265b38be88ad52a3de87b1582e5bfe.jpg
    htmls = soup.find_all('a')  # 获取所有的img
    # print(imgs)
    for html in htmls:
        # 'http:\/\/www.xiaohuar.com\/p-1-2005.html'
        url = html['href']
        url = url.replace('\\', '') #取消字符串中所有的反斜杠\
        # 'http://www.xiaohuar.com/p-1-2005.html'
        url = url.replace('p-1', 's-1')
        # print(url)
        res = requests.get(url, headers=header)
        # print(res.text)
        html3 = res.text
        soup = BeautifulSoup(html3, 'html.parser', from_encoding='gbk')
        # https://wx.dxs6.cn/api/xiaohua/upload/min_img/20180918/201809189fxSpDRUad.jpg
        imgs = soup.find_all('img', src=re.compile(r'api/xiaohua/upload/min_img/\d+/\w+\.jpg'))  # 获取所有的img
        # print(imgs)
        for img in imgs:
            # 'http:\/\/www.xiaohuar.com\/p-1-2005.html'
            url = img['src']
            # print(url)
            req = request.Request(url=url, headers=header)
            # 获得了我们的图片信息
            data = request.urlopen(req, timeout=10).read()
            print(data)
            inter_time = time.time()
            j = j + 1
            with open('G:\PaChong\A6\ %s.jpg' % j, 'wb') as f:
                f.write(data)


