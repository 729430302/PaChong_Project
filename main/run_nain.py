# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# auth：Yan
from Base.get_data import Getdata
from Data.data_config import Global_values

class Run():

    # 定义全局变量
    def __init__(self):
        self.get_data = Getdata()
        self.value = Global_values()
        self.url = self.value.url

    # 主程序
    def run(self):
        self.get_data.main(self.url)


if __name__ == '__main__':
    Run().run()
