# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import os
import random
import re
import threading
from bs4 import BeautifulSoup
import requests


os.makedirs('E:/PaChong/meinvtupian1', exist_ok=True)
path = 'E:\PaChong\meinvtupian1\ %s.gif'

def header():
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1", \
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3", \
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3", \
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24", \
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
    ]
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


def main(num1, num2):
    for i in range(num1, num2, -1):
        url = 'https://www.ffyybba.com/' + str(i) + '.html'
        res = requests.get(url=url, headers=header(), verify=False
                           )
        if res.status_code == 200:
            response = res.content
            soup = BeautifulSoup(response, 'html.parser', from_encoding='gbk')
            gifs = soup.find_all('img', src=re.compile(r'http.*?\.gif'))  # 获取所有的img
            gifs2 = soup.find_all('img', src=re.compile(r'http.*?\.jpg'))  # 获取所有的img
            for gif in gifs:
                gif_url = gif['src']
                gif_name = gif_url.replace('\\', '').replace('/', '').replace(':', '')[:-3]
                res = requests.get(url=gif_url, headers=header(), verify=False
                                   )
                if res.status_code == 200:
                    gif_response = res.content
                    log = '正在下载：' + str(gif_name) + '，地址：' + str(gif_url)
                    with open('E:/PaChong/log1.txt', 'a', encoding='utf-8') as f:
                        f.writelines(log)
                        f.write('\n')
                    # print(log)
                    with open(path % gif_name, 'wb') as f:
                        f.write(gif_response)
            for gif2 in gifs2:
                gif_url2 = gif2['src']
                gif_name2 = gif_url2.replace('\\', '').replace('/', '').replace(':', '')[:-3]
                res = requests.get(url=gif_url2, headers=header(), verify=False
                                   )
                if res.status_code == 200:
                    gif_response2 = res.content
                    log = '正在下载：' + str(gif_name2) + '，地址：' + str(gif_url2)
                    with open('E:/PaChong/log1.txt', 'a', encoding='utf-8') as f:
                        f.writelines(log)
                        f.write('\n')
                    # print(log)
                    with open(path % gif_name2, 'wb') as f:
                        f.write(gif_response2)

if __name__ == '__main__':
    y = 0
    for i in range(440, 36, -10):
        y = y + 1   # 计数的
        j = i - 10
        t = threading.Thread(target=main, args=(i, j))
        print('第' + str(y) + '个线程，下载第' + str(i) + '~' + str(j) + '页资源，开始下载~~')
        print()
        t.start()
