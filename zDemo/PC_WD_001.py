import random
import re
import threading

import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

url = 'http://www.umei.cc/meinvtupian/meinvmote/180316.htm'


# 获取所以UA的haeder
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


# 获取HTML内容
def get_response(url, proxies=None):
    res = requests.get(url=url, headers=header(), verify=False,
                       proxies=proxies
                       )
    if res.status_code == 200:
        response = res.content
        return response


# 解析HTML并获取相关元素集合
def get_htmls1(response1):
    soup = BeautifulSoup(response1, 'html.parser', from_encoding='gbk')
    imgs = soup.find_all('img', src=re.compile(r'/picture/\d+/\w+/\d\.jpg'))  # 获取所有的img
    # imgs2 = soup.find_all('a', class_='nry')
    return imgs


# 解析HTML并获取相关元素集合
def get_htmls2(response2):
    doc = pq(response2)
    igms = doc.find('.relax-arc .ajax_ul li a img')
    igms_list = igms.items()
    return igms_list


# 遍历HTML中获取的元素列表
def for_list1(igms_list):
    for img in igms_list:
        url1 = img.attr.src
        name1 = img.attr.title
        print(url1)
        print(name1)
        start_save_img(url1, name1)  # 调用多线程
        save_img(url1, name1)  # 调用下载方法


# 遍历HTML中获取的元素列表
def for_list2(imgs):
    for img in imgs:
        img_url = img['src']
        res = requests.get(url=img_url, headers=header(), verify=False)
        img = res.content
        name = img_url.replace('\\', '').replace('/', '').replace(':', '')[:-3]
        start_save_img(img, name)  # 调用多线程
        # self.save_img(img, name)    # 调用下载方法


# 下载资源方法
def save_img(img, name):
    with open('F:\PaChong\A1\ %s.jpg' % name, 'wb') as f:
        f.write(img)


# 多线程
def start_save_img(img, name):
    th = threading.Thread(target=save_img, args=(img, name))
    th.start()

# 判断是否下载和保存相同内容
def if_txt(gif_url2):
    with open('E:/PaChong/log1.txt', "r", encoding='utf-8') as f:  # 设置文件对象
                    str_num2 = f.read()  # 可以是随便对文件的操作
                    if str(gif_url2) in str_num2:   #判断文件内容是否包含当前URL
                        print('已存在')
                    else:
                        pass#执行保持内容 、请求接口、 下载  操作