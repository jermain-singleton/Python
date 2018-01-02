""" My first attempt at a web crawler"""


# calls my modules needed that are not builtin
import requests
from bs4 import BeautifulSoup


# main function
def trade_spider(max_pages):
    page = 1
    for i in range(1, max_pages+1):
        url = 'https://www.buya.com/Store/SAM-S-LOCKER/400?page={}'.format(i) #http/?...
        source_code = requests.get(url)
        plain_text = source_code.content
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('h3', {'class': "two-lines-name"}):  # loops through variable 
            href = link.a["href"]
            print(href)
        
trade_spider(2)
