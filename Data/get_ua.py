# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# auth：
import time

import requests
from bs4 import BeautifulSoup

from Tools.get_txt import Gettxt


class Getua:
    def __init__(self):
        self.get_txt = Gettxt()

    def pa_ua(self):
        for a in range(1, 20):
            page = int(a)
            url1 = "http://www.fynas.com/ua/search?d=&b=&k=&page=%s/ " % page
            # URL ="http://www.fynas.com/ua/search?d=&b=%E5%BE%AE%E4%BF%A1&k=&page=50"

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Cookie': 'Hm_lvt_0fa7b8c467469bd8f2eaddd5dc1d440d=1544148446; Hm_lpvt_0fa7b8c467469bd8f2eaddd5dc1d440d=1544148638',
                'Host': 'www.fynas.com',
                'Referer': 'http://www.fynas.com/ua/search?d=&b=&k=&page=2',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }

            html = requests.get(url=url1, headers=headers)

            time.sleep(0.5)
            html.encoding = "utf-8"

            coun = html.text

            soup = BeautifulSoup(coun, "lxml")

            tdTags = soup.find_all("td")  # 获取所有td标签内容
            for ua in tdTags:  # 遍历每个便签
                ua = str(ua)[4:-5]  # 去掉前后标签保留内容
                if 'Mozilla/5.0' in ua:  # 筛选包好'Mozilla/5.0'的内容
                    if 'Windows' in ua:
                        print(ua)
                        self.get_txt.read2('ua.txt')


if __name__ == '__main__':
    a = Getua().pa_ua()
