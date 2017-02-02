import os
import logging
from urllib.request import urlopen
import youtube_dl
from bs4 import BeautifulSoup
def download(title, video_url):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
text="starboy"
query = '+'.join(text.lower().split())
url = 'https://www.youtube.com/results?search_query=' + query
content = urlopen(url).read()
soup = BeautifulSoup(content, 'html.parser')
tag = soup.find('a', {'rel': 'spf-prefetch'})
title = tag.text
video_url = 'https://www.youtube.com' + tag.get('href')
download(title,video_url)
