# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-

import os
import random
import re
import threading

import requests
from bs4 import BeautifulSoup

os.makedirs('F:/PaChong/meinvtupian', exist_ok=True)

def main(url, path, num1, num2):
    for a in range(num1, num2):
        if a != 1:
            url_name = url.replace('1.htm', '') + str(a) + '.htm'
        else:
            url_name = url
        res = requests.get(url=url_name, headers=header(), verify=False)

        if res.status_code == 200:
            response1 = res.content

            soup = BeautifulSoup(response1, 'html.parser', from_encoding='gbk')
            # 'http://www.umei.cc/meinvtupian/waiguomeinv/183696.htm'
            htmls = soup.find_all('a', href=re.compile(r'/meinvtupian/\w+/\d+\.htm'))  # 获取所有的html

            for html in htmls:
                i = 0
                for n in range(1, 50):
                    img_url1 = html['href'][:-4] + '_' + str(n) + '.htm'

                    res = requests.get(url=img_url1, headers=header(), verify=False)
                    if res.status_code == 200:
                        response2 = res.content

                        soup = BeautifulSoup(response2, 'html.parser', from_encoding='gbk')
                        'http://i1.umei.cc/uploads/tu/201812/10135/cz1894da9z.jpg'
                        'http://i1.umei.cc/uploads/tu/201608/7/nmenwztuvu5.jpg'
                        imgs = soup.find_all('img', src=re.compile(r'/uploads/tu/\d+/\d+/\w+\.jpg'))  # 获取所有的html

                        for img in imgs:
                            i = i + 1
                            img_url2 = img['src']
                            name = img_url2.replace('\\', '').replace('/', '').replace(':', '')[:-4]

                            res = requests.get(url=img_url2, headers=header(), verify=False)
                            if res.status_code == 200:
                                response3 = res.content

                                with open(path % name, 'wb') as f:
                                    f.write(response3)


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
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36']
    UserAgent = random.choice(user_agent_list)
    headers = {'User-Agent': UserAgent}
    return headers


# encoding: utf-8

import requests
import re
import time
time1 = time.time()
main_url = 'http://video.eastday.com/a/170612170956054127565.html'
resp = requests.get(main_url)
#没有这行，打印的结果中文是乱码
resp.encoding = 'utf-8'
html = resp.text
link = re.findall(r'var mp4 = "(.*?)";', html)[0]
link = 'http:'+link
dest_resp = requests.get(link)
#视频是二进制数据流，content就是为了获取二进制数据的方法
data = dest_resp.content
#保存数据的路径及文件名
path = u'F:/赵丽颖.mp4'
f = open(path, 'wb')
f.write(data)
f.close()
time2 = time.time()
print(u'ok,下载完成!')
print(u'总共耗时：' + str(time2 - time1) + 's')



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

    # main(url='http://www.umei.cc/meinvtupian/1.htm', path='F:\PaChong\meinvtupian\ %s.jpg', num1=1, num2=250)

    # t1 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 1, 10))
    # t1.start()
    #
    # t2 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 11, 20))
    # t2.start()
    #
    # t3 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 21, 30))
    # t3.start()
    #
    # t4 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 31, 40))
    # t4.start()
    #
    # t5 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 41, 50))
    # t5.start()
    #
    # t6 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 51, 60))
    # t6.start()
    #
    # t7 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 61, 70))
    # t7.start()
    #
    # t8 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 71, 80))
    # t8.start()
    #
    # t9 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 81, 90))
    # t9.start()
    #
    # t10 = threading.Thread(target=main,
    #                        args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 91, 100))
    # t10.start()
    #
    # t11 = threading.Thread(target=main,
    #                        args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 101, 110))
    # t11.start()
    #
    # t12 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 1, 10))
    # t12.start()
    #
    # t13 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 11, 20))
    # t13.start()
    #
    # t14 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 21, 30))
    # t14.start()
    #
    # t15 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 31, 40))
    # t15.start()
    #
    # t5 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 41, 50))
    # t5.start()
    #
    # t6 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 51, 60))
    # t6.start()
    #
    # t7 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 61, 70))
    # t7.start()
    #
    # t8 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 71, 80))
    # t8.start()
    #
    # t9 = threading.Thread(target=main,
    #                       args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 81, 90))
    # t9.start()
    #
    # t10 = threading.Thread(target=main,
    #                        args=('http://www.umei.cc/meinvtupian/1.htm', 'F:\PaChong\meinvtupian\ %s.jpg', 91, 100))
    # t10.start()
    # y = 0
    # for i in range(1, 250, 10):
    #     y = y + 1
    #
    #     j = i + 10
    #     t = threading.Thread(
    #         target=main,
    #         args=(
    #             'http://www.umei.cc/meinvtupian/1.htm',
    #             'F:\PaChong\meinvtupian\ %s.jpg',
    #             # 'F:\PaChong\A1\ %s.jpg',
    #             i,
    #             j
    #         )
    #     )
    #     print('第' + str(y) + '个线程开始')
    #     t.start()
    pass

