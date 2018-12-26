# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# auth：Yan
import random

from Tools.get_txt import Gettxt


class Global_values:
    ip_file_add = '../Data/ip.txt'
    ua_file_add = '../Data/ua.txt'
    save_file_add = 'F:\PaChong\A1\ %s.jpg'
    url = 'http://www.tu11.com/qingchunmeinvxiezhen/2018/14220.html'

    def ip_value(self):
        get_txt = Gettxt()
        value = Global_values()
        ip_list = get_txt.read1(value.ip_file_add)
        ip = random.choice(ip_list)
        return ip

    def ua_value(self):
        get_txt = Gettxt()
        value = Global_values()
        UA_list = get_txt.read1(value.ua_file_add)
        ua = random.choice(UA_list)
        return ua


if __name__ == '__main__':
    ip = Global_values().ip_value()
    ua = Global_values().ua_value()
    print(ip)
    print(ua)
