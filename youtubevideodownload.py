import re
import requests
from bs4 import BeautifulSoup
from VideoDown import VideoDown

#选择方式：1,单个视频下载 2,列表视频下载

choose = 1
while(choose):
    print("*"*30)
    choose = int(input("1,单个视频下载\n2,列表视频下载\n0,退出\n" + "*"*30 + "\n"))
    if choose == 1:
        print("你选择了下载单个视频\n")

        url = input('输入下载网址\n')
        filename= input('输入保存的文件名\n')
        video_down = VideoDown(url,filename)
        video_download_url = video_down.getVideoDownloadUrl()
        video_down.writeFile2(video_download_url)

    elif choose==2:
        print("你选择了下载列表视频\n")
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
        i = 1
        for item in soup_select:
            if item['href'].startswith('/watch'):
                item_text_replace = item.text.strip(' \n')
                if '#' in item.text:
                    item_text_replace = item_text_replace.replace('#', '')
                    print(item_text_replace)
                if '?' in item.text:
                    item_text_replace = item_text_replace.replace('?', '')
                    print(item_text_replace)
                nameList.append(item_text_replace + '\n')
                video_down = VideoDown(format % item['href'], str(i))
                video_download_url = video_down.getVideoDownloadUrl()
                urlList.append(video_download_url + '\n')
                video_down.writeFile(video_download_url)
                i += 1

        file = open('videoUrl.txt', 'w')
        for item in urlList:
            file.write(item)

        file.close()
        file = open('videoName.txt', 'w')
        for item in nameList:
            file.writelines(item)

        file.close()


