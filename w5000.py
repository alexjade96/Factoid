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
with open(temp, 'w+') as f:
	f.write(r.text)

#with open(temp) as o:
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
Since Dec 15, 2015 (close before Fed Reserve raised int rates for 1st time since June 29 2006) w5000 up x percent or y t/billiongit 
Since Sept 12 2012 close before Bernanke revealed QE3, w5000 up x y 
Since Aug 26 2010 close before Bernanke revealed QE2, w5000 up x y
w5000 up x y from the Financial Crisis low of Mar 9 2009
Since old Oct 9 2007 Market high, w5000 up x y
'''
