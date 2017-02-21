import requests
from bs4 import BeautifulSoup
import re


class MySpider():
    def __init__(self,path):
        self.start_url = path


    # 索引页链接获取，参数m索引页类型，n索引页第几页
    def getIndexPath(self,m,n):

        if n == 1:
            indexPath = self.start_url + 'list/index' + str(m) + '.html'
        else:
            indexPath = self.start_url + 'list/index' + str(m) + '_' + str(n) + '.html'
        return indexPath

    # 索引页中列表内容获取：item链接，标题，图片链接
    def getItems(self,m,n):
        indexPath = self.getIndexPath(m,n)
        response = requests.get(indexPath)
        response.encoding = 'gbk'
        # print(response.text)

        soup = BeautifulSoup(response.text, 'html.parser')
        # soup = BeautifulSoup(url,'html.parser')
        address = []
        title = []
        img = []

        for item in soup.select('.list-pianyuan-box'):
            temp = item.select('a')[0]
            # print(item.select('a'))
            href = self.start_url + 'player' + temp['href'][5:] + '?' + temp['href'][11:16] + '-0-0'
            address.append(href)
            title = temp['title']
            img = self.start_url + item.select('a > img')[0]['src']  # a标签下img子标签
            # print(href,title,img)

        return [address,title,img]

    def getItemContent(self,itempath):
        # x = 1
        # itemContent = []
        # for playItem in itempath:
        #     print(x)
        #     x += 1
        response = requests.get(itempath)
        response.encoding = 'gbk'
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(response.text)
        tem = soup.select('.playbox2-c')[0].select('script')[0]['src']
        # print(tem)
        aresult = self.start_url + tem
        # result.append(aresult)
        # print(tem[1]['src'])

        response = requests.get(aresult)
        response.encoding = 'gbk'
        # print(response.text)
        temp = response.text
        left = temp.find('$') + 1
        if temp.count('$') == 2:
            right = temp.find(']') - 8
            # print(temp[left:right])
            return temp[left:right]
            # file.writelines(temp[left:right] + '\n')
        else:
            temp = temp[left:]
            right = temp.find(',') - 8
            # print(temp[:right])
            return temp[:right]
            # file.writelines(temp[:right] + '\n')
            # print(result)


path = 'http://www.xfa69.com/'
sp = MySpider(path)
result = sp.getItems(1,3)
print(result[0])
for aResult in result[0]:
    item = sp.getItemContent(aResult)
    print(item)

# print(item)
