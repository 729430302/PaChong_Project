#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import os
import threading

os.makedirs('G:/PaChong/MeiTu/xiaoha', exist_ok=True)

def main(num1, num2):

    start_url = 'http://www.xiaohuar.com/p-6-'
    for i in range(num1, num2):
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
        imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+\.jpg'))
        print(imgs)

        for img in imgs:
            # 创建一个请求
            # "/d/file/20170707/f7ca636f73937e33836e765b7261f036.jpg"
            url = "http://www.xiaohuar.com%s" % img['src']
            req = request.Request(url=url, headers=header)
            # 获得了我们的图片信息
            data = request.urlopen(req).read()
            # 保存图片
            name = url.replace('\\', '').replace('/', '').replace(':', '')
            with open('G:\PaChong\MeiTu\/xiaoha\ %s.jpg' % name, 'wb') as f:
                f.write(data)


if __name__ == '__main__':
    y = 0
    for i in range(1, 46, 1):
        y = y + 1  # 计数的

        j = i + 1
        t = threading.Thread(target=main, args=(i, j))
        print('第' + str(y) + '个线程，下载第' + str(i) + '~' + str(j) + '页资源，开始下载~~')
        print()
        t.start()
