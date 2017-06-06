#!/usr/bin/env python
# coding: utf-8

import urllib
from bs4 import BeautifulSoup
import os

# url
url = 'http://jandan.net/ooxx/page-2397#comments'

res = urllib.urlopen(url)
html = res.read()

soup = BeautifulSoup(html, 'html.parser')
result = soup.find_all('img')

links = []
for content in result:
    links.append('http:' + content.get('src'))

if not os.path.exists('photo'):
    os.makedirs('photo')

i = 0

for link in links:
    i += 1
    fileName = './photo/' + 'photo' + str(i) + '.png'
    print(link)
    with open(fileName, 'w') as file:
        urllib.urlretrieve(link, fileName)

