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
Day
Month
Quarter
'''

def hist_comp(value):
'''
Jan 20 2017

Nov 8 2016

Jan 26 2018

Feb 11 2016

Dec 15 2015

Sept 12 2012

Aug 26 2010

Mar 9 2009

Oct 9 2007

'''
