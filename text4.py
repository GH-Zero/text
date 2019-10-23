import requests
url='https://jx.618g.com/?url=https://www.iqiyi.com/v_19rttqe45s.html#vfrm=19-9-0-1'
text=requests.get(url).text
print(text)

ffmpeg-i'网址' -vcodec copy -copy 名字.mp4
