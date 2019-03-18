from bs4 import BeautifulSoup
import requests
from lxml import *
import re


def get_url(url,header):
    if url == 'http://www.ty76.com/192088.shtml':
        r = requests.get(url, headers=header)
        r.encoding = 'GBK'
        soup = BeautifulSoup(r.text, 'lxml').find('span')
        for geturl in soup:
            geturl = geturl.get('href')
            return geturl
    else:
        r = requests.get(url, headers=header)
        r.encoding = 'GBK'
        soup = BeautifulSoup(r.text,'lxml').find_all('a',text='下一页')
        for geturl in soup:
            geturl = geturl.get('href')
            return geturl


def download(url,header,cou):
    r = requests.get(url, headers=header)
    r.encoding = 'GBK'
    soup = BeautifulSoup(r.text,'lxml').find_all('div',id="content" ,class_="content")
    title = BeautifulSoup(r.text,'lxml').find('div',class_='title').string
    title = str(title[11:])
    for soup in soup:
        text = soup.get_text()
        f = open('路径'+ str(cou) +'.'+ title +'.txt','w',encoding='utf-8')
        f.write('\n\n\n' + text)
        f.close()
        print('第'+ str(cou) +'章下载完毕')


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
url = 'http://www.ty76.com/192088.shtml'
geturl = get_url(url,header)
cou=1

while geturl != 'http://www.ty76.com/modules/article/lastchapter.php?aid=192088&dynamic=1':
    download(geturl,header,cou)
    geturl = get_url(geturl,header)
    cou=cou+1