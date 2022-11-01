import urllib.request as req
url="https://securepubads.g.doubleclick.net/static/topics/topics_frame.html"
# 建立一個Request物件，附加request header的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
with req.urlopen(url) as response:
    data=response.read().decode("utf-8")
print(data)