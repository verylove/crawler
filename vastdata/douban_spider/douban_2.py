#encoding: utf-8

import requests
from bs4 import BeautifulSoup
import json

def get_page():
    # 1. url
    url = "https://movie.douban.com/cinema/nowplaying/changsha/"
    # 2. 请求页面的时候应该发送什么数据
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }
    # 3. GET/POST请求
    # 采用的是GET请求

    # 4. 发送请求
    response = requests.get(url, headers=headers)
    text = response.text
    return text

def parse_page(text):
    soup = BeautifulSoup(text,'lxml')
    # data-category=nowplaying
    # attribute
    liList = soup.find_all("li",attrs={"data-category":"nowplaying"})
    for li in liList:
        print(li)
        print('='*30)

if __name__ == '__main__':
    text = get_page()
    parse_page(text)