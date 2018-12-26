# encoding:utf-8
#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
import requests
import re
from bs4 import BeautifulSoup
from multiprocessing.pool import Pool


class MaiZi():

    def __init__(self):
        # 你要抓去的url
        self.url = 'http://www.maiziedu.com/course/572/'

    # 解析url的函数
    def parse_next_url(self):
        request = requests.get(self.url)
        request.encoding = request.apparent_encoding  # 设置编码格式
        for url in BeautifulSoup(request.text, 'html.parser').select('ul.lesson-lists li a'):
            next_url = 'http://www.maiziedu.com/' + url['href']  # 每个页面的url
            yield next_url

    # 解析内容的url
    def parse_content(self, url):
        request = requests.get(url)  # 解析每个页面视频的url
        request.encoding = request.apparent_encoding  # 设置编码方式
        demo = '\$lessonUrl = "(.*?)"'  # 找到MP4的位置
        de = re.compile(demo, re.S)
        url_next = de.findall(request.text)[0]  # 得到视频的链接
        title = BeautifulSoup(request.text, 'html.parser').select('span.selected')[0]['name']  # 视频的名称
        content = requests.get(url_next).content  #  解析视频
        print('开始写入:', title)
        print('---------------')
        with open('F:\\PaChong\\' + title + '.mp4', 'wb') as e:
            e.write(content)
            print('写入完成:', title)
            print('---------------')
    # 线程
    def parse_pool(self):
        pool = Pool(4)
        pool.map(self.parse_content, self.parse_next_url())
        pool.close()


if __name__ == '__main__':
    Run = MaiZi()
    a = Run.parse_content('http://www.maiziedu.com/course/572 - 8106 /')
    print(a)

