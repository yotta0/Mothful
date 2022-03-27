import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup()

html = requests.get("")


bs = BeautifulSoup(html, 'html.parser')
print(bs.h1)

