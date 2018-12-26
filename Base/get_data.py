# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# auth：Yan
import re
import threading

import requests
from bs4 import BeautifulSoup

from Data.data_config import Global_values
from Tools.get_txt import Gettxt


class Getdata():

    # 定义全局变量
    def __init__(self):
        self.values = Global_values()
        self.get_txt = Gettxt()
        self.ip = self.values.ip_value()
        self.ua = self.values.ua_value()
        self.proxies = {'http': self.ip}
        self.header = {'User-Agent': self.ua}

    # 获取HTML内容
    def get_response(self, url):
        res = requests.get(url=url, headers=self.header, verify=False,
                           proxies=self.proxies
                           )
        response = res.content
        return response

    # 解析HTML并获取相关元素集合
    def get_htmls(self, response):
        soup = BeautifulSoup(response, 'html.parser', from_encoding='gbk')
        imgs = soup.find_all('img', src=re.compile(r'/picture/\d+/\w+/\d\.jpg'))  # 获取所有的img
        # imgs2 = soup.find_all('a', class_='nry')
        return imgs

    # 遍历HTML中获取的元素列表
    def for_list(self, imgs):
        for img in imgs:
            img_url = img['src']
            res = requests.get(url=img_url, headers=self.header, verify=False)
            img = res.content
            name = img_url.replace('\\', '').replace('/', '').replace(':', '')[:-3]
            self.start_save_img(img, name)  # 调用多线程
            # self.save_img(img, name)    # 调用下载方法

    # 下载资源方法
    def save_img(self, img, name):
        with open(self.values.save_file_add % name, 'wb') as f:
            f.write(img)

    # 多线程
    def start_save_img(self, img, name):
        th = threading.Thread(target=self.save_img, args=(img, name))
        th.start()

    # 主程序
    def main(self, url):
        response = self.get_response(url)
        htmls = self.get_htmls(response)
        self.for_list(htmls)


if __name__ == '__main__':
    url = 'http://www.tu11.com/qingchunmeinvxiezhen/2018/14220.html'
    pc = Getdata()
    pc.main(url)
