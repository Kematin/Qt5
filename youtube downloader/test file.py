from bs4 import BeautifulSoup
import urllib.request
import requests
import json
import wget


headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
        }
video_url = 'https://youtu.be/gvYGIhuiJQI?list=PL8L3o_bRFhHIjI1QmHL4xwGtZYFzAC8l1'        
file = 'dolbaeb.mp4'

def donwload_video(url, file_name):

    req = requests.get(url=url, stream=True)

    with open(file_name, 'wb') as file:
        for chunk in req.iter_content(chunk_size=1024 * 1024):
            if chunk:
                file.write(chunk)

    return 'Download finish!'



def for_wget(url, file_name):
    wget.download(url=url, out=file_name)
    print('sssssss')

for_wget(video_url, file)