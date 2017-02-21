# http://172.87.27.31/search.asp?page=2&searchword=%B2%BD%B1%F8&searchtype=-1
# 带关键词爬去
import urllib.parse

import requests
from bs4 import BeautifulSoup

dress = []
name = []
imagPath = []
keyword = input('请输入搜索关键词：')
keywordUrlcode = urllib.parse.quote(keyword.encode(encoding='gbk'))
m = int(input('输入爬取得页面数：'))
print('预计爬取链接数目为%d'%(m*10))
for i in range(1,m+1):
    url = 'http://172.87.27.31/search.asp?page=' + str(i) + '&searchword=' + keywordUrlcode + '&searchtype=-1'
    # print(url)
    response = requests.get(url)
    response.encoding = 'gbk'
    # print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    for item in soup.select('li'):
        if (len(item.select('img')) > 0):
            # dress = item.select('a')[0]['href']
            # name = item.select('img')[0]['alt']
            # imagPath = item.select('img')[0]['src']
            # print(dress,name, imagPath)
            dress.append(item.select('a')[0]['href'])
            name.append(item.select('img')[0]['alt'])
            imagPath.append(item.select('img')[0]['src'])

print(dress)
print(name)
print(imagPath)
print(len(imagPath))
