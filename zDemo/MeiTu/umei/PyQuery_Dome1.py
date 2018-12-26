# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import os
import random
import threading

import requests
from pyquery import PyQuery as pq

os.makedirs('E:/PaChong/meinvtupian', exist_ok=True)


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

'''检测IP是否可用'''
def checkip():
    with open('../Data/ip.txt', 'r', encoding='utf-8') as f:
        ip_list = []
        for s in f.readlines():
            ip_list.append(s.strip())

    with open('ipvalues.txt', 'w', encoding='utf-8') as f:
        f.truncate()
    for ip in ip_list:
        proxies = {"http": "http://" + ip, "https": "http://" + ip}  # 代理ip
        try:
            response = requests.get(url='http://www.umei.cc/meinvtupian/1.htm', proxies=proxies, headers=header(), timeout=5, verify=False)
            # print(response.status_code)
            if response.status_code == 200:
                print('ok')

                with open('ipvalues.txt', 'a', encoding='utf-8') as f:
                    f.writelines(ip)
                    f.write('\n')
        except:
            print('ip：' + ip + '无法使用')



def ip():
    with open('ipvalues.txt', 'r', encoding='utf-8') as f:
        ip_list = []
        for s in f.readlines():
            ip_list.append(s.strip())

    ip_value = random.choice(ip_list)
    return ip_value


def main(url, path, num1, num2):
    for a in range(num1, num2):
        if a != 1:
            url_name = url.replace('1.htm', '') + str(a) + '.htm'
        else:
            url_name = url

        res = requests.get(url=url_name, headers=header(), verify=False,
                            # proxies={'http': ip()}
                           )
        if res.status_code == 200:
            response1 = res.content

            doc1 = pq(response1)
            imgs1 = doc1.find('.TypeBigPics')
            imgs_list1 = imgs1.items()

            for img in imgs_list1:
                html = img.attr('href')

                res = requests.get(url=html, headers=header(), verify=False,
                                   # proxies={'http': ip()}
                                   )
                if res.status_code == 200:
                    response2 = res.content

                    doc2 = pq(response2)
                    num_values = doc2.find('.NewPages ul li a')
                    num_value = int(str(num_values)[3:7].replace('共', '').replace('页', '').replace(':', ''))
                    # print(num_value)

                    i = 0
                    for n in range(1, num_value + 1):
                        i = i + 1
                        if n != 1:
                            img_url1 = html[:-4] + '_' + str(n) + '.htm'
                        else:
                            img_url1 = html

                        res = requests.get(url=img_url1, headers=header(), verify=False,
                                           # proxies={'http': ip()}
                                           )
                        if res.status_code == 200:
                            response3 = res.content

                            doc3 = pq(response3)
                            imgs2 = doc3.find('#ArticleId22 p a img')
                            if imgs2 == '':

                                imgs2 = doc3.find('#ArticleId22 p img')
                            img = imgs2.attr('src')
                            name = str(imgs2.attr('alt')) + str(i)

                            if img == None:
                                imgs2 = doc3.find('#ArticleId22 p img')
                                img = imgs2.attr('src')
                                name = str(imgs2.attr('alt')) + str(i)


                            log = '正在下载：' + str(name) + '，地址：' + str(img)

                            with open('E:/PaChong/log.txt', 'a', encoding='utf-8') as f:
                                f.writelines(log)
                                f.write('\n')

                            print(log)
                            '''============================================================================'''
                            res = requests.get(url=img, headers=header(), verify=False,
                                               # proxies={'http': ip()}
                                               )
                            if res.status_code == 200:
                                response4 = res.content

                                with open(path % name, 'wb') as f:
                                    f.write(response4)


if __name__ == '__main__':
    # 'http://www.umei.cc/meinvtupian/1.htm'    250
    # 'http://www.umei.cc/meinvtupian/xingganmeinv/1.htm'   77
    # 'http://www.umei.cc/meinvtupian/siwameinv/1.htm'       23
    # 'http://www.umei.cc/meinvtupian/meinvxiezhen/1.htm'   39
    # 'http://www.umei.cc/meinvtupian/waiguomeinv/1.htm'    25
    # 'http://www.umei.cc/meinvtupian/nayimeinv/1.htm'      21
    # 'http://www.umei.cc/meinvtupian/jiepaimeinv/1.htm'    9
    # 'http://www.umei.cc/meinvtupian/meinvzipai/1.htm'    24
    # 'http://www.umei.cc/meinvtupian/rentiyishu/1.htm'     12
    # 'http://www.umei.cc/meinvtupian/meinvmote/1.htm'      23
    # 'http://www.umei.cc/meinvtupian/zhifumeinv.htm'       1

    # main(url='http://www.umei.cc/meinvtupian/1.htm',
    #      path='F:\PaChong\A1\ %s.jpg',
    #      num1=1, num2=2)



    # print(checkip())


    y = 0
    for i in range(1, 250, 3):
        y = y + 1   # 计数的

        j = i + 3
        t = threading.Thread(
            target=main,
            args=(
                'http://www.umei.cc/meinvtupian/1.htm',
                'E:\PaChong\meinvtupian\ %s.jpg',
                # 'F:\PaChong\A1\ %s.jpg',
                i,
                j
            )
        )
        print('第' + str(y) + '个线程，下载第' + str(i) + '~' + str(j) + '页资源，开始下载~~')
        print()
        t.start()
