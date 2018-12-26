# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import os
import random

import threading

import requests
from pyquery import PyQuery as pq

os.makedirs('F:/PaChong/FengYueBa', exist_ok=True)
path = 'F:\PaChong\FengYueBa\ %s.gif'


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
        n_list = []
        u_list = []
        url = 'https://www.ffyybba.com/' + str(i) + '.html'
        res = requests.get(url=url, headers=header(), verify=False
                           )
        if res.status_code == 200:
            response = res.content

            doc = pq(response)
            gif_names = doc.find('.main p')
            gif_urls = doc.find('.main p img')

            name_list = gif_names.items()
            url_list = gif_urls.items()

            for name in name_list:
                g_name = name('p').text()
                if g_name:
                    n_list.append(g_name)
                    # print(g_name)

            for url in url_list:
                g_url = url.attr('src')
                u_list.append(g_url)
                # print(g_url)

            for (n_name, u_url) in zip(n_list, u_list):

                res = requests.get(url=u_url, headers=header(), verify=False)
                if res.status_code == 200:
                    gif_response = res.content
                    log = '正在下载：' + str(n_name) + '，地址：' + str(u_url)
                    with open('F:/PaChong/FengYueBa_log.txt', 'a', encoding='utf-8') as f:
                        f.writelines(log)
                        f.write('\n')
                    print(log)
                    with open(path % n_name, 'wb') as f:
                        f.write(gif_response)


if __name__ == '__main__':
    y = 0
    for i in range(440, 36, -5):  # 36
        y = y + 1  # 计数的
        j = i - 5
        t = threading.Thread(target=main, args=(i, j))
        print('第' + str(y) + '个线程，下载第' + str(i) + '~' + str(j) + '页资源，开始下载~~')
        print()
        t.start()
