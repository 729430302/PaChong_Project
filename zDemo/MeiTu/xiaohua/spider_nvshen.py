#!/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
import os
import requests
import time

class Spider:

    def __init__(self):

        self.url = "http://www.xiaohuar.com/nvshen/"
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    # 根据url获取网页的html
    def git_html(self, url=None):
        try:
            res = requests.get(url=url, headers=self.header, verify=False)
            html = res.content
            return html
        except Exception as e:
            print('git_html_error=%s' % e)

    # 根据html获取html中所有图片链接，列表形式
    def git_imgs(self, html=None):
        try:
            soup = BeautifulSoup(html, 'html.parser', from_encoding='gbk')
            # http://www.xiaohuar.com/d/file/20151120/fd265b38be88ad52a3de87b1582e5bfe.jpg
            imgs = soup.find_all('img', src=re.compile(r'/d/file/\d+/\w+\.jpg'))    # 获取所有的img
            return imgs
        except Exception as e:
            print('git_imgs_error=%s' % e)


    # 根据图片资源保存到本地
    def save_img(self, data=None):
        inter_time = time.time()
        try:
            with open('G:\PaChong\A5\ %s.jpg' % inter_time, 'wb') as f:
                f.write(data)
        except Exception as e:
            print('save_img_error=%s' % e)

    # 根据所有图片链接，获取到图片资源
    def git_jpg(self, imgs=None):
        try:
            for img in imgs:
                # "/d/file/20170707/f7ca636f73937e33836e765b7261f036.jpg"
                url = 'http://www.xiaohuar.com' + img['src']
                req = request.Request(url=url, headers=self.header)
                # 获得了我们的图片信息
                data = request.urlopen(req, timeout=10).read()
                # print(data)
                self.save_img(data)
        except Exception as e:
            print('git_jpg_error=%s' % e)

    # 主函数
    def run(self):
        html = self.git_html(self.url)
        # print(html)
        if html:
            imgs = self.git_imgs(html)
            # print(imgs)
        else:
            print('html的值为空')
        if imgs:
            self.git_jpg(imgs)
        else:
            print('imgs的值为空')


if __name__ == '__main__':
    os.makedirs('G:/PaChong/A7', exist_ok=True)
    s = Spider()
    s.run()
