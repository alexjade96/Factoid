from bs4 import BeautifulSoup
import requests
import urllib2
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

json_file = "w5000.json"
url = "https://finance.google.com/finance?q=INDEXNYSEGIS:W5000&output=json"
data = urllib2.urlopen(url)
with open(json_file, 'w+') as f:
	for line in data:
		f.write(line)


temp = "test.txt"
r = requests.get(url)
with open(temp, 'a+') as f:
	f.write(r.text)

with open(temp) as o:
	#print json.dumps(json.loads(url), indent=4, sort_keys=True)
	
'''
======
Specs:
======
Closed at x Day/week Up or down by points & percent
Paper gain/loss ([T/B]illion)
Rose/fell x day/week in a row in the past y days/weeks
For the month/quarter w5000 is up/down x percent or y t/billion
Since Jan 20, 2017 (Trump Inauguration) w5000 has gained/lost x percent or y t/billion
Since Nov 8, 2016 (2016 Election) w5000 has gained/lost x percent or y t/billion
Since Last market high (currently Jan 26, 2018) w5000 is up/down x percent or y t/billion
Since Dec 15, 2015 (

'''
