from http import client
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

url = "https://news.google.com/news/rss"
client = urlopen(url)
xml_page = client.read()
client.close()
soup_page = soup(xml_page, 'lxml')
news_list = soup_page.find_all('item')

for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print('-'*60)