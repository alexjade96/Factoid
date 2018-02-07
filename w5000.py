from bs4 import BeautifulSoup
import requests
import sys,os
import json

#Site: https://finance.yahoo.com/quote/%5EW5000?p=%5EW5000
#Historical: https://finance.yahoo.com/quote/%5EW5000/history?p=%5EW5000
#Parsers: html.parser, lxml, lxml-xml, html5lib

#Google URL: https://finance.google.com/finance?q=INDEXNYSEGIS:W5000&output=json
url = "https://finance.yahoo.com/quote/%5EW5000/history?p=%5EW5000"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

print soup#.find("div",{"id":"Lead-2-QuoteHeader-Proxy"})



