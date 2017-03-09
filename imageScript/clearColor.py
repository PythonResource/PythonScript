#!/usr/bin/env python
# coding: utf-8

import sys
import os

from PIL import Image

imgPath = '/Users/xiexiaolong1/pythonCode/source/launchImage.png'
img = Image.open(imgPath)

img.thumbnail((128,128), Image.ANTIALIAS)
img.save('/Users/xiexiaolong1/pythonCode/source/hehe.JPEG','JPEG')

img.show()