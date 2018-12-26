# ！/usr/bin/env/ python3
# -*- coding: utf-8 -*-
# auth：Yan


class Gettxt:

    # ------------------------------------------------------文档处理--------------------------------------------------------
    # 写入文档
    def write(self, path, text):
        with open(path, 'a', encoding='utf-8') as f:
            f.writelines(text)
            f.write('\n')

    # 清空文档
    def clear(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            f.truncate()

    # 读取文档
    def read1(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            txt = []
            for s in f.readlines():
                txt.append(s.strip())
        return txt

    # ----------------------------------------------------------------------------------------------------------------------
