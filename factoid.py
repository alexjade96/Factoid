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
print df.head()
#print df.tail()
print df[9715:9721]

