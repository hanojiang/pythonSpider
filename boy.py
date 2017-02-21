import requests
from bs4 import BeautifulSoup


net = 'http://www.xfa69.com/'
dress = []
for i in range(1,2):
    if i == 1:
        url = net + 'list/index1.html'
    else:url = net + 'list/index1_' + str(i) +'.html'

    print(url)

    response = requests.get(url)
    response.encoding = 'gbk'
    # print(response.text)

    soup = BeautifulSoup(response.text,'html.parser')
    # soup = BeautifulSoup(url,'html.parser')
    for item in soup.select('.list-pianyuan-box'):
        temp = item.select('a')[0]
        # print(item.select('a'))
        href = net + '/player' + temp['href'][5:] + '?' + temp['href'][11:16] + '-0-0'
        dress.append(href)
        title = temp['title']
        img = net + item.select('a > img')[0]['src']#a标签下img子标签
        # print(href,title,img)
    # sel = soup.select('.list-pianyuan-box')[0]
    # href = sel.select('a')[0]['href']
    # title = sel.select('a')[0]['title']
    # img = sel.select('a > img')[0]['src']
    # # print(type(select))
# print(img)
x = 1
file = open('c.txt','w')
result = []
# print(dress)
for playItem in dress:
    print(x)
    x += 1
    response = requests.get(playItem)
    response.encoding = 'gbk'
    soup = BeautifulSoup(response.text,'html.parser')
    # print(response.text)
    tem = soup.select('.playbox2-c')[0].select('script')[0]['src']
    # print(tem)
    aresult = net + tem
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
