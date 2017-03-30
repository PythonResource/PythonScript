#!/usr/bin/env python
# coding: utf-8

import sys
import os

from PIL import Image

# if len(sys.argv) < 3 :
#     print ('\033[31m' + '请输入正确命令,eg: \'python clearColor.py /path/xxx.png\'' + '\033[0m')
#     quit()

imgPath = '/Users/xiexiaolong1/pythonCode/source/launchImage.png'
img = Image.open(imgPath)

# img.thumbnail((128,128), Image.ANTIALIAS)
# img.save('/Users/xiexiaolong1/pythonCode/source/hehe.JPEG','JPEG')

img.transpose(Image.FLIP_LEFT_RIGHT)

img.show()