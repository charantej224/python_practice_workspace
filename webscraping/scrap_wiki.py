import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Neural_network"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

VALID_TAGS = ['div', 'p']
text_list = []
for tag in soup.findAll('p'):
    if tag.name in VALID_TAGS:
        text_list.append(tag.get_text())
print("".join(text_list))
