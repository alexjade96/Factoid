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
