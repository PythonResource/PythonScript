# -*- coding: utf-8 -*-

from PIL import Image,ImageDraw
import random

def randomColor():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

width, height = 750, 1334

im = Image.new('RGB', (width, height), randomColor())

image = ImageDraw.Draw(im)

for x in range(width):
    for y in range(height):
        if x%30 == 0 or y%30 == 0:
            image.point((x,y),fill=(255,255,255))
im.show()