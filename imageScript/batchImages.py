#!/usr/bin/env python
# coding: utf-8

import sys
import os
import copy
import glob
import time
import threading

from PIL import Image

suffix = 'jpg'

# 生成缩略图
def resizeImageAndSave(imagePath, outPutPath, (width, height)):
    print('正在处理' + imagePath)
    originImg = ''
    try:
        originImg = Image.open(imagePath)
    except:
        print ('\033[31m' + '\'' + '图片路径: ' + imagePath + '\'' + '，该文件不是图片文件，请检查文件路径.' + '\033[0m')
        return

    extension = os.path.basename(imagePath)
    imageName, ext = os.path.splitext(extension)
    # print('file = ' + imageName + ', ext = ' + ext)

    img0 = originImg.copy()
    img1 = originImg.copy()
    img2 = originImg.copy()

    img0.thumbnail((width, height), Image.ANTIALIAS)
    img1.thumbnail((width * 2, height * 2), Image.ANTIALIAS)
    img2.thumbnail((width * 3, height  * 3), Image.ANTIALIAS)

    img0.save(os.path.join(outPutPath, imageName + '.png'), "png")
    img1.save(os.path.join(outPutPath, imageName + '@2x.png'), "png")
    img2.save(os.path.join(outPutPath, imageName + '@3x.png'), "png")

# 遍历文件加下的图片文件
def scanImages(imageDirectory, outPutPath, (width, height)):

    if not os.path.exists(imageDirectory):
        print ('\033[31m' + '\'' + '文件夹路径: ' + imageDirectory + '\'' + '不存在' + '\033[0m')
        return

    imageList = glob.glob1(imageDirectory, '*.%s'%suffix)

    threads = []
    for image in imageList:
        imagePath = os.path.join(imageDirectory,image)
        t = threading.Thread(target=resizeImageAndSave, args=(imagePath, outPutPath, (width, height)))
        threads.append(t)
        # resizeImageAndSave(imagePath, outPutPath, (width, height))

    for t in threads:
        t.start()
        while True:
            # 控制线程数量
            if len(threading.enumerate()) <= 10:
                break


# 获取当前时间
def getNowTime():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

if __name__ == '__main__':

    if len(sys.argv) < 4:
        print (
        '\033[31m' + '请输入正确命令,eg: \'python %s /images/directory 20 30\',表示把图片重置为宽20高30的图片'%sys.argv[0] + '\033[0m')
        quit()

    imageDirectory = sys.argv[1]
    size = (int(sys.argv[2]), int(sys.argv[3]))
    # imageDirectory = '/Users/xiexiaolong1/Desktop/images/paper'
    # size = (100, 100)

    # 输出路径准备
    userDir = os.path.expanduser('~')
    desktopDir = os.path.join(userDir, 'Desktop')
    outPutPath = os.path.join(desktopDir, 'images'+ getNowTime())
    print(outPutPath)
    if not os.path.exists(outPutPath):
        os.makedirs(outPutPath)

    # 浏览图片并生成缩略图
    scanImages(imageDirectory, outPutPath, size)


    # imageName = '/Users/xiexiaolong1/Desktop/images/paper/331.jpg'
    # resizeImageAndSave(imageName, outPutPath,(80, 80))
