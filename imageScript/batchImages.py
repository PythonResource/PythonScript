# !/usr/bin/env python
# coding: utf-8

# 简介: 批量生成书略图, 适用于iOS开发生成@1x, @2x, @3x 缩略图
# 用法: 终端执行: python /path/script.py /path/images/directory 20 30
# 说明: 20 30 为生成的缩略图为等比的, 例如: 400x500会生成,  20x25, 40x50, 60x75 三张缩略图

import sys
import os
import copy
import glob
import time
import threading

try:
    from PIL import Image
except:
    print ('\033[31m' + 'Missing Image module, installing Image module, please wait ...' + '\033[0m')
    success = os.system('python -m pip install Image')
    if success == 0:
        print('\033[7;32m' + 'Image module installed successfully.' + '\033[0m')
        from PIL import Image
    else:
        print (
            '\033[31m' + 'Image installation failed, please execute manually at terminal：\'python -m pip install Image\'re-install.' + '\033[0m')
        quit()

# 控制线程数, 保证速度与性能
ThreadNumber = 10


# 生成缩略图
def resizeImageAndSave(imagePath, outPutPath, size):
    print('Converting ' + imagePath)
    originImg = ''
    try:
        originImg = Image.open(imagePath)
    except:
        print (
            '\033[31m' + 'image path: ' + '\'' + imagePath + '\'' + '. The file is not an image file, please check the file path.' + '\033[0m')
        return

    extension = os.path.basename(imagePath)
    imageName, ext = os.path.splitext(extension)
    # print('file = ' + imageName + ', ext = ' + ext)

    img0 = originImg.copy()
    img1 = originImg.copy()
    img2 = originImg.copy()

    img0.thumbnail((width, height), Image.ANTIALIAS)
    img1.thumbnail((width * 2, height * 2), Image.ANTIALIAS)
    img2.thumbnail((width * 3, height * 3), Image.ANTIALIAS)

    img0.save(os.path.join(outPutPath, imageName + '.png'), "png")
    img1.save(os.path.join(outPutPath, imageName + '@2x.png'), "png")
    img2.save(os.path.join(outPutPath, imageName + '@3x.png'), "png")


# 遍历文件加下的图片文件
def scanImages(imageDirectory, outPutPath, size):
    imageList = glob.glob1(imageDirectory, '*')

    threads = []
    print ('fuck')
    for image in imageList:
        imagePath = os.path.join(imageDirectory, image)
        t = threading.Thread(target=resizeImageAndSave, args=(imagePath, outPutPath, (width, height)))
        threads.append(t)
        # resizeImageAndSave(imagePath, outPutPath, (width, height))

    for t in threads:
        t.setDaemon(True)
        t.start()
        while True:
            # 控制线程数量
            if len(threading.enumerate()) <= ThreadNumber:
                break

    print('\033[7;32m' + 'Batch images finished.' + '\033[0m')
    os.system('open ' + outPutPath)


# 获取当前时间
def getNowTime():
    return time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))


if __name__ == '__main__':

    if len(sys.argv) < 4:
        print (
            '\033[31m' + 'Command error,eg: \'python %s /images/directory 20 30\', means generate thumbnails to 20x30' %
            sys.argv[0] + '\033[0m')
        quit()

    imageDirectory = sys.argv[1]

    width = 0
    height = 0
    try:
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    except:
        print ('\033[31m' + '\'python %s /images/directory 20 30\'.' % sys.argv[
            0] + 'The last two parameters must be numbers.' + '\033[0m')
        quit()

    size = (width, height)

    if not os.path.exists(imageDirectory):
        print (
            '\033[31m' + 'Directory path: ' + '\'' + imageDirectory + '\'' + r" don't exist, please check it." + '\033[0m')
        quit()

    # 输出路径准备
    userDir = os.path.expanduser('~')
    desktopDir = os.path.join(userDir, 'Desktop')
    outPutPath = os.path.join(desktopDir, 'images' + getNowTime())
    print(outPutPath)
    if not os.path.exists(outPutPath):
        os.makedirs(outPutPath)

    # 浏览图片并生成缩略图
    scanImages(imageDirectory, outPutPath, size)
