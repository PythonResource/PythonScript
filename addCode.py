#!/usr/bin/env python
# coding: utf-8

import sys
import os

fileName = sys.argv[1]

def dealLine(line):


try:
    if os.path.isfile(fileName):  ## 判断文件是否存在

        f = open(fileName)
        try:
            lines = f.readlines()

            for line in lines:
                dealLine(line)

                ## input()
        finally:
            f.close()

    else:
        print('File does not exists.')
        ##input()
except:
    print('Input Error!')