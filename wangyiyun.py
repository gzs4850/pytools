#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 8:54
# @Author  : z.g

import requests
from lxml import html

# 抖音排行榜链接
# url = 'https://music.163.com/playlist?id=2250011882'
# 热歌榜
url = 'https://music.163.com/playlist?id=3778678'
# 外链转换链接（https://link.hhtjim.com/）
base_url = 'https://link.hhtjim.com/163/'

# 设置请求头
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
}
# 访问链接
result = requests.get(url, headers=header).text
# print(result)

# 提取id 和 name
etree = html.etree
dom = etree.HTML(result)
ids = dom.xpath("//a[contains(@href,'/song?')]/@href")
names = dom.xpath("//a[contains(@href,'/song?')]/text()")

# 遍历音乐
for id, name in zip(ids, names):
    if ("$" in id) == False:
        id = id.strip("/song?id=")
        # print(id, name)
        # 获取单个音乐链接
        song_url = base_url + id + '.mp3'
        # print(song_url)
        # 访问获取音乐文件
        music = requests.get(song_url).content

        # 保存音乐
        with open('E:/music/%s.mp3' %name, 'wb') as file:
            file.write(music)
        print("下载歌曲 %s 完成" %name)

