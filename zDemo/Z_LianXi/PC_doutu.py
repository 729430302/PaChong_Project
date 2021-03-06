#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
import requests,threading
import lxml.etree
from bs4 import BeautifulSoup
'''
1、先获取html源码方法stream
2、获取资源连接，并用连接获取源码
3、获取图片url，或者资源url
4、通过图片连接下载图片，或通过url下载资源
5、增加多线程
'''

#通过请求获取html源码
def get_html(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    res = requests.get(url=url, headers=header, verify=False)
    # print(res.text)   #打印源码
    return res.content  # 获取源码


#找到图片的超链接获取源码
def get_img_hmtl(html):
    soup = BeautifulSoup(html, 'lxml')  #解析网页方式，自带  html.parser
    all_a = soup.find_all('a', class_='list-group-item random_list')    #找到a标签
    for i in all_a:
        # print(i)  #链接
        img_html = get_html(url=(i['href']))
        # print(img_html)     #打印源码
        get_img(html=img_html)

#获取图片的url
def get_img(html):
    soup = lxml.etree.HTML(html)    #初始化源代码，自动修正代码
    items = soup.xpath('//div[@class="artile_des"]')    #@选取属性
    for item in items:
        imgurl_list = item.xpath('table/tbody/tr/td/a/img/@onerror')
        # print(imgurl_list)  #打印图片连接
        # imgurl_list = str(imgurl_list)
        # save_img(imgurl_list)           #单线程下载
        start_save_img(imgurl_list)     #多线程下载


#下载
x = 0 #命名
#拼接完整连接，文件open
def save_img(img_url):
    global x
    x += 1
    img_url = img_url.split('=')[-1][1:-2].replace('jp', 'jpg')      #[1:-2]取消第一个字符  和倒数两个字符
    print('正在下载' + 'http:' + str(img_url) + '\n')
    img_text = requests.get(img_url).content
    with open('D:/%s.jpg' % x, 'wb')as f:
        f.write(img_text)

#多线程
def start_save_img(imgurl_list):
    for i in imgurl_list:
        # print(i)
        th = threading.Thread(target=save_img, args=(i,))
        th.start()

#多页
def mian():
    start_url = 'http://www.doutula.com/article/list/?page='
    for i in range(1, 20):
        start_html = get_html(start_url.format(i))  #获取多页
        get_img_hmtl(html=start_html)    #获取图片所在的连接源码


if __name__ == '__main__':
    mian()

