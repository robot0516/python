from aip import AipSpeech
import os
import requests
from lxml import etree

def getAudioContent(resultFile,resultStr):
    APP_ID = '16531802'
    API_KEY = 'BRMvO0hWaFmQ06siF2QvK8BK'
    SECRET_KEY = 'ozqPjNF5K5iplbLIghyzGgrGhISgbTa7'

    resultFile=r"E:\auido.mp3" 
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    
    resultStr=resultStr
    result  = client.synthesis(
        resultStr, 
        'zh', 1, {
                    'vol': 8,#音量
                    'per':5,#0 女 1 男 3逍遥 4萝莉
                    'spd':3,#语速
                    'pit':8#语调
                }
    )
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open(resultFile, 'wb') as f:
            f.write(result) 
    os.system(resultFile)

def getContent(url,encoding):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        #"Referer":"https://www.meitulu.com/img.html"#针对no-referrer-when-downgrade反爬虫防盗链解决办法
    }
    res=requests.get(url,headers=headers)
    #print("请求状态码%s"%res.status_code)
    res.encoding=encoding
    return res.content

def getXpathContent(url,encoding,xpath):
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
        #"Referer":"https://www.meitulu.com/img.html"#针对no-referrer-when-downgrade反爬虫防盗链解决办法
    }
    res=requests.get(url,headers=headers)
    #print("请求状态码%s"%res.status_code)
    res.encoding=encoding
    text=res.text
    html=etree.HTML(text)
    xpathContent=html.xpath(xpath)
    return xpathContent

if __name__ == '__main__':
    resultFile=r"E:\auido.mp3" 
    #filename=os.path.splitext(resultFile)#分离文件名和扩展名
    url="http://news.baidu.com/"
    encoding="utf-8"
    xpath1="//div[@id='pane-news']/div/ul/li[contains(@class,'hdline')]/strong/a/text()"
    xpath2="//div[@id='pane-news']/div/ul/li[contains(@class,'hdline')]/strong/a/@href"
    titles=getXpathContent(url,encoding,xpath1)
    urls=getXpathContent(url,encoding,xpath2)
    print(titles)
    contentStr=""
    for url in urls:
        xpath="/html/body/div[7]/div[3]/div[1]/p/text()"
        content=getXpathContent(url,encoding,xpath)
        for c in content:
            contentStr=contentStr+c

getAudioContent(resultFile,contentStr[:600])