import re
import shutil
import urllib.parse
import urllib.request

import requests

class VideoDown():

    def __init__(self,videoUrl,fileName):
        self.videoUrl = videoUrl
        self.fileName = fileName + '.mp4'
        print(self.fileName)

    # def getCorrectFileName(self,fileName):
    #     for c in [' ','/','\\',':','*','"','<','>','|','?','\n']:
    #         if c in fileName:
    #             fileName.replace(c,'')
    #     return fileName
    def getVideoDownloadUrl(self):
        response = requests.get(self.videoUrl)
        re_search = re.search('"url_encoded_fmt_stream_map":".*?(url=.*?)quality', response.text)
        print(re_search.group(1))
        qs = urllib.parse.parse_qs(re_search.group(1))
        index = qs['url'][0].find('\\u')
        downloadUrl = qs['url'][0][:index]

        if ',' in downloadUrl:
            download_url_find = downloadUrl.find(',')
            downloadUrl = downloadUrl[:download_url_find]
        return downloadUrl

    def writeFile(self,downloadUrl):
        f = open(self.fileName, 'wb')

        res2 = requests.get(downloadUrl, stream=True)
        shutil.copyfileobj(res2.raw, f)

        # urllib.request.urlretrieve(downloadUrl,self.fileName)

        f.close()




# url = input('输入下载网址')
# filename= input('输入保存的文件名')
# video_down = VideoDown(url,filename)
# video_download_url = video_down.getVideoDownloadUrl()
# video_down.writeFile(video_download_url)
