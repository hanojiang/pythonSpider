import re
import requests
from bs4 import BeautifulSoup

from VideoDown import VideoDown

startUrl = input('输入列表网址：')
response = requests.get(startUrl).text

soup = BeautifulSoup(response, 'html.parser')
soup_select = soup.select('a[dir="ltr"]')
format = 'https://www.youtube.com%s'


# def correctName(text):
#     text.strip(' /\\:*"<>|?\n')
#     return text
urlList = []
nameList = []

for item in soup_select:
    if item['href'].startswith('/watch'):
        item_text_replace = item.text.strip(' \n')
        if '#' in item.text:
            item_text_replace = item_text_replace.replace('#', '')
            print(item_text_replace)
        if '?' in item.text:
            item_text_replace = item_text_replace.replace('?', '')
            print(item_text_replace)
        nameList.append(item_text_replace + '\n' )
        video_down = VideoDown(format % item['href'], item_text_replace)
        video_download_url = video_down.getVideoDownloadUrl()
        urlList.append(video_download_url + '\n')
        # video_down.writeFile(video_download_url)

        # print(format % item['href'])
        # print(item.text.strip())

# file = open('videoUrl.txt','w')
# for item in urlList:
#     file.write(item)
#
# file.close()
file = open('videoName.txt','w')
for item in nameList:
    file.writelines(item)

file.close()





# select = soup.select('h4')
#
# name = []
# i=0
# for item in select:
#     if item.string != '':
#         name.append(item.string.strip(' /\\:*"<>|?\n'))#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
#     print(name[i])
#     i += 1
# format = 'https://www.youtube.com%s'
# i=0
# for item in search:
#     print(item)
    # print(i)

    # video_down = VideoDown(format % item, name[i])
    # video_download_url = video_down.getVideoDownloadUrl()
    # video_down.writeFile(video_download_url)
    # i += 1