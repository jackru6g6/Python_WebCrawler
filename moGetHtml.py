# import re #正規表達視
# from bs4 import BeautifulSoup
# from urllib.request import urlopen

# website = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
# html = urlopen(website).read().decode('utf-8')

# soup = BeautifulSoup(html,features='lxml')
# print(soup.h1)
# print('\n',soup.p)

# allHref = soup.find_all('a')
# for l in allHref:
#     print(l['href'])

from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='lxml')

# use class to narrow search
month = soup.find_all('li', {"class": "month"})
for m in month:
    print(m.get_text())


jan = soup.find('ul', {"class": 'jan'})
d_jan = jan.find_all('li')              # use jan as a parent
for d in d_jan:
    print(d.get_text())