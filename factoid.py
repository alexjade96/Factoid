import pandas as pd
import datetime
import requests
import urllib2
import sys,os
import json
import time
import csv

'''
Factoid Possible Headers:

A) Date
B) Value at Close
C) Change from last day
D) % Change from last day
E) Change from last month
F) % Change from last month
G) Change from last Quarter
H) % Change from last Quarter
I) Current Market High
J) Recent Market Low

'''

xl_file = "Wilshire Factoid Worksheet.xlsx"
sheet1 = "201801xx"

xl = pd.ExcelFile(xl_file)
xl.sheet_names
df = xl.parse(sheet1)
df.head()

dates = [
	datetime.datetime.strftime("%Y%m%d"),
	datetime.datetime.strftime("%Y%m01"),

]


#df has -2 rows (For Column Title & index row 0)
#print df.head()
print df.tail(22)
df.dropna(thresh=2)
print df.tail(22)
#print df[9715:9721]
#print df[:-22].dropna(thresh=2)

#Use [Max - 27] to get latest Date
'''
1) Define & use formulas outside of xlsx worksheet/inside script
2) Use COM/win32 to use existing Excel formulas (win dev only)
3) Generate new table/spreadsheet with strict definition for easier data manip.
'''

#input: close value, date
#use: historical values (yesterday, last month, last quarter)
#output: Range of comparison values 

def close_compare(close_value, operand_value):
	
	#Return (percentage change, money value difference)

def statement(VAL_DATE,VAL_PERCENT,VAL_DOLLAR):
	dat = lambda d: datetime.datetime.strptime(str(d),'%Y%m%d').strftime("%B %d, %Y")
	mod = lambda x: "up " + str(x) if x >= 0 else "down " + str(x)
	dol = lambda y: str(float(y/1000.0)) + " trillion" if y >= 1000 else str(y) + " billion"
	print "Since " + dat(VAL_DATE) + ", the Wilshire 5000 is " + mod(VAL_PERCENT) + " percent, or approximately $" + dol(VAL_DOLLAR)

'''
Day close
get_close_value()
Month-month end
datetime.datetime.strftime("%m")
Quarter-quarter end
if datetime.datetime.strftime("%m") % 3:
	pre-val = get [datetime.datetime.strftime("%m") - 3]
	
'''

def hist_comp(value):
'''
Store Recent High/Recent Low
Jan 26 2018
current-high = 0
high-date = yyyymmdd
For line in file:
	if line[index-for-current-high] > current-high:
		current-high = line[index-for-current-high]
		high-date = line[date-for-current-high]
Feb 11 2016
current-low = 0
low-date = yyyymmdd
For line in file:
	if line[index-for-current-low] > current-low:
		current-low = line[index-for-current-low]
		low-date = line[date-for-current-low]

Jan 20 2017 "the close on the day of the Trump Inauguration"
D9475
23744.73

Nov 8 2016 "the close on the day of the 2016 Election"
D9426
22165.78

Dec 15 2015 "the close before the Federal Reserve raised interest rates for the first time since June 29, 2006"
D9199
21099.58

Sept 12 2012 "the close before Bernanke revealed QE2"
D8380
15038.58

Aug 26 2010 "the close before Bernanke revealed QE3"
D7864
10973.00

Mar 9 2009 "the financial Crisis low"
D7493
6858.43
(20090309,6858.43)
Oct 9 2007 "the old market high"
D7138
15806.69
(20071009,15806.69)
'''
