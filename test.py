import requests
from bs4 import BeautifulSoup
import json

url = 'https://zingmp3.vn/album/Top-100-Bai-Hat-Nhac-Tre-Hay-Nhat-Various-Artists/ZWZB969E.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
post_elements=soup.find(id='root')
all_post=list(post_elements.children)


# with open('all_post.json', 'wt', encoding='utf-8') as f:
#    f.write(json.dumps(all_post, ensure_ascii=False))
