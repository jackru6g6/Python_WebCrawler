import requests
import re #正規表達視
from bs4 import BeautifulSoup
from urllib.request import urlopen


def getWebpage(url):

    htmlpage = requests.get(url)
    htmlpage.encoding = 'utf-8'


    if htmlpage.status_code != 200:
        print("Error")
        return None
    else:
        #return htmlpage.text.encode(encoding="utf-8", errors="strict")
        return htmlpage.text

#site = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.26310500%201558319808"
site = "https://morvanzhou.github.io/static/scraping/basic-structure.html"
html = getWebpage(site)
print(html)