# -*- coding: utf-8 -*-
import re

from yufan import Request

"""
喜马拉雅扒MP3
准备需要下载的列表页的url，自动下载全部mp3
"""

# 喜马拉雅的url
url = "http://www.ximalaya.com/1000202/album/9723091"

# 头信息
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q = 0.8",
    "Cache-Control": "max - age = 0",
    "Connection": "keep - alive",
    "Cookie": "_xmLog=xm_1517811162122_jd9tks22cbjxrk;trackType=web;x_xmly_traffic=utm_source%3A%26utm_medium"
              "%3A%26utm_campaign%3A%26utm_content%3A%26utm_term%3A%26utm_from%3A"
              ";Hm_lvt_4a7d8ec50cfd6af753c4f8aee3425070=1517811163;Hm_lpvt_4a7d8ec50cfd6af753c4f8aee3425070"
              "=1517825590;_ga=GA1.2.231886250.1517811163",
    "Host": "www.ximalaya.com",
    "Referer": "http://www.ximalaya.com/search/all/kw/%E9%83%AD%E5%BE%B7%E7%BA%B2/page/1/sc/true",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0(WindowsNT10.0;WOW64)AppleWebKit/537.36(KHTML, "
                  "likeGecko)Chrome/59.0.3071.115Safari/537.36 "
}


# 获取列表页最大页码
def page_max(url):
    try:
        text = Request.get(url=url, headers=headers).text
        page_max = re.findall(re.compile(u"unencode>(.*?)<", re.S), text)[-1]
        return url, page_max
    except:
        return False


# 喜马拉雅下载mp3类
class Ximalaya(object):
    def __init__(self, url, page):
        self.num = 0
        self.page_num = 1
        self.play_path_list = []
        self.url = url + "?page=" + str(page)
        self.play_url = 'https://www.ximalaya.com/tracks/'

    # 获取当前页id
    def get_sound_id(self):
        print "抓取id中......"
        id = Request.get(url=self.url, headers=headers)
        text = id.text
        ids = re.findall(re.compile(u'sound_ids="(.*?)"', re.S), text)[0]
        self.ids = ids.split(',')
        self.names = re.findall(re.compile(u'hashlink title="(.*?)"', re.S), text)[1:-3]
        print "id抓取完毕......"

    # 获取需要下载的url
    def get_play_path(self):
        print "准备下载的url......"
        for x in self.ids:
            url = self.play_url + str(x) + '.json'
            play_path = Request.get(url=url, headers=headers).json()["play_path_64"]
            self.play_path_list.append(play_path)
        print "下载的url准备完毕......"

    # 下载
    def down(self):
        print "开始下载......"
        for url in self.play_path_list:
            r = Request.get(url=url, stream=True)
            with open('D:\A123\\' + self.names[self.num] + '.m4a', 'wb') as f:
                if self.num < len(self.ids):
                    self.num += 1
                    r.iter_content()
                for chunk in r.iter_content(chunk_size=1024 * 1024):
                    if chunk:
                        f.write(chunk)
            print self.num - 1, self.names[self.num - 1], "downloaded"


# 主函数，按页下载
def main(url):
    if page_max(url):
        url, pagemax = page_max(url)
        for page in xrange(1, int(pagemax) + 1):
            print "=====抓取第", page, "页====="
            xi = Ximalaya(url, page)
            xi.get_sound_id()
            xi.get_play_path()
            xi.down()
        print "all downloaded!"
    else:
        print "=====抓取====="
        xi = Ximalaya(url, 1)
        xi.get_sound_id()
        xi.get_play_path()
        xi.down()
        print "all downloaded!"


if __name__ == '__main__':
    main(url)