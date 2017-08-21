# -*- coding: utf-8 -*-

import webbrowser
import time

def main():
    path = '/Users/xiexiaolong1/Desktop/DataSource/test/m'
    target = '/Users/xiexiaolong1/Desktop/allm.mp3'

    ft = open(target, 'a')

    for i in range(0, 4):
        source = path + str(i) + '.mp3'
        fs = open(source, 'rb')
        ft.write(fs.read())



if __name__ == u"__main__":
    main()
