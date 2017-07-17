# -*- coding:utf-8 -*-
import requests,threading
from  bs4 import BeautifulSoup


def contentUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
    reponse = requests.get(url, headers=headers)

    content = reponse.content

    return content
def getImageList(url):


    content = contentUrl(url)
    # print(content.decode("utf-8"))#将bytes （Unicode）转为utf-8

    soup = BeautifulSoup(content,"html.parser")
    imageUrlList=[]
    for item in soup.findAll("img", { "class" : "lazy image_dtb" }):
        imageUrlList.append("http://" + item['data-original'].replace("//",""))

    # print(imageUrlList)
    return  imageUrlList




def downimage(url):
    print("downloading***********%s"%url)
    imgecontent = requests.get(url).content
    with open("./doutu2/%s.jpg" % url.split("/")[-1],'wb') as f:
        f.write(imgecontent)

def start_urlList(urlList):
    for url in urlList:
        th1 = threading.Thread(target=downimage,args=(url,))
        th1.start()

start_url = "https://www.doutula.com/article/list/?page={0}"
for i in range(1,200):
    urlList = getImageList(start_url.format(i))
    start_urlList(urlList)