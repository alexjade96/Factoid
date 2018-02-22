import pandas as pd
import requests
import urllib2
import sys,os
import json
import csv

xl_file = "Wilshire Factoid Worksheet.xlsx"
sheet1 = "201801xx"

xl = pd.ExcelFile(xl_file)
xl.sheet_names
df = xl.parse(sheet1)
df.head()

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

def term(value):
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

Jan 20 2017 (Trump Inaug)
D9475
23744.73
Nov 8 2016
D9426
22165.78
Dec 15 2015
D9199
21099.58
Sept 12 2012
D8380
15038.58
Aug 26 2010
D7864
10973.00
Mar 9 2009
D7493
6858.43
Oct 9 2007
D7138
15806.69
'''
