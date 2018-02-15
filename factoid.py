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
Month-month end
Quarter-quarter end
'''

def hist_comp(value):
'''
Store Recent High/Recent Low
Jan 26 2018

Feb 11 2016


Jan 20 2017
D9475
Nov 8 2016
D9426
Dec 15 2015
D9199
Sept 12 2012
D8380
Aug 26 2010
D7864
Mar 9 2009
D7493
Oct 9 2007
D7138
'''
