# -*- coding: utf-8 -*-
import re
import shutil
import urllib.parse

import requests

from bs4 import BeautifulSoup


def getVideoDownloadUrl(videoUrl):
    response = requests.get(videoUrl)
    re_search = re.search('"url_encoded_fmt_stream_map":".*?(url=.*?)quality',response.text)
    print(re_search.group(1))
    qs = urllib.parse.parse_qs(re_search.group(1))
    index = qs['url'][0].find('\\u')
    downloadUrl = qs['url'][0][:index]

    if ',' in downloadUrl:
        download_url_find = downloadUrl.find(',')
        downloadUrl = downloadUrl[:download_url_find]
    return downloadUrl

def writeFile(fileName,downloadUrl):
    res2 = requests.get(downloadUrl, stream=True)
    filename = fileName + '.mp4'
    f = open(filename, 'wb')
    shutil.copyfileobj(res2.raw, f)
    f.close()

response = requests.get('https://www.youtube.com//watch?v=ceUhb2-gYOU&amp;index=1&amp;list=PLohb4k71XnPaQRTvKW4Uii1oq-JPGpwWF').text
search = re.findall('<a\shref="(.*?)"\sclass="\sspf-link',response)
# search1 = re.findall('class="yt-ui-ellipsis\syt-ui-ellipsis-2">(.*?)\</h4',response) 不会整
soup = BeautifulSoup(response, 'html.parser')
select = soup.select('h4')
name = []
i=0
for item in select:
    if item.string != '':
        name.append(item.string.strip(' /\\:*"<>|?\n'))#Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
    print(name[i])
    i += 1
format = 'https://www.youtube.com%s'
i=0
for item in search:
    writeFile(name[i],getVideoDownloadUrl(format%item))
    i += 1

# writeFile('[爬蟲實戰] 如何使用Selenium 自動將slides.com 的網頁投影片輸出成圖檔',getVideoDownloadUrl('https://www.youtube.com/watch?v=uS1HYKHMuDQ'))