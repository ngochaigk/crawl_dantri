import requests
from bs4 import BeautifulSoup
import json

url = 'https://zingmp3.vn/album/Top-100-Bai-Hat-Nhac-Tre-Hay-Nhat-Various-Artists/ZWZB969E.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
post_elements=soup.find(id='root')
song=list(post_elements.children)


# with open('song.json', 'wt', encoding='utf-8') as f:
#    f.write(json.dumps(song, ensure_ascii=False))
