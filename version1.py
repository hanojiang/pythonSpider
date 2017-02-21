from bs4 import BeautifulSoup
import requests
import urllib.request
dress = []
name = []
imagPath = []

# 爬索引页的图片名字，地址，下载页地址。并将下载页地址保存到文件a.txt中。
m = int(input('输入爬取得页面数：'))
print('预计爬取链接数目为%d'%(m*16))
for i in range(1,m+1):
    if i == 1:
        path = 'http://aqdyam.com/lusi/index.html'
    else:path = 'http://aqdyam.com/lusi/index' + str(i) +'.html'
    print(path)
    response = requests.get(path)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'html.parser')

    for item in soup.select('li'):
        if(len(item.select('img')) > 0):
            dress.append('http://aqdyam.com' + item.select('a')[0]['href'] + 'player-0-0.html')
            name.append(item.select('img')[0]['alt'])
            imagPath.append(item.select('img')[0]['src'])
# print(dress[0])
# dress中得到单个播放网址

x = 1
result = []
file = open('b.txt','w')
# print(dress)
for playItem in dress:
    print(x)
    x += 1
    response = requests.get(playItem)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'html.parser')
    tem = soup.select('body script[type="text/javascript"]')#body标签下，匹配type属性的script标签
    # print(tem)
    aresult = 'http://aqdyam.com' + tem[1]['src']
    result.append(aresult)
    # print(tem[1]['src'])

    response = requests.get(aresult)
    response.encoding = 'gbk'
    # print(response.text)
    temp = response.text
    left = temp.find('$') + 1
    if temp.count('$') == 2:
        right = temp.find(']') - 8
        print(temp[left:right])
        file.writelines(temp[left:right] + '\n')
    else:
        temp = temp[left:]
        right = temp.find(',') - 8
        print(temp[:right])
        file.writelines(temp[:right] + '\n')
# print(result)

file.close()
