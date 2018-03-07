from datetime import timedelta
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
xl_file = "Wilshire Factoid Template.xlsx"
sheet1 = "201801xx"

xl = pd.ExcelFile(xl_file)
xl.sheet_names
df = xl.parse(sheet1)
df.head()

specs = [
	20071009,
	20090309,
	20100826,
	20120912,
	20151215,
	20160211,
	20161108,
	20170120,
	20180126,
	20180219,
	20180220,
	20180221,
	int(datetime.datetime.now().strftime("%Y%m01")),
	int((datetime.datetime.today() - timedelta(days=1)).strftime("%Y%m%d")),
	int(datetime.datetime.now().strftime("%Y%m%d"))
]

for item in specs:
	print type(item),item
#for item in specs:
	#print type(item),item
	#print df['Wilshire 5000 (Full Cap) Price'].str.contains(item)#.isin(comparisons)
#print df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)]
temp = df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)].iloc[:,0:4]
print temp
for i in range(0,temp.shape[0]):
	for j in range(0,temp.shape[1]):
		print "("+str(i)+","+str(j)+")",df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)].iloc[i,j]

test = df[df.iloc[:,0].isin(specs)].iloc[:,[0,3]]
print test
for n in range(0,test.shape[0]):
	print type(test.iloc[n,0]),test.iloc[n,0],type(test.iloc[n,1]),test.iloc[n,1]

lambda input,desc: float(1.00 - input/desc)

def append_line(df):
	test_insert = pd.DataFrame(df[-1:].values, index=[int(df.last_valid_index())+1], columns=df.columns)
	df = df.append(test_insert)
	print df.tail(2)
#append_line(df)
'''for index, row in df.iterrows():
	for line in comparisons:
		if line in str(row):
			print row'''
#print df.tail(22)
#df.dropna(thresh=2)
#print df.tail(22)
#print df[9715:9721]
#print df[:-22].dropna(thresh=2)

#Use [Max - 27] to get latest Date
#yesterday = df.tail(1)
'''
1) Define & use formulas outside of xlsx worksheet/inside script
2) Use COM/win32 to use existing Excel formulas (win dev only)
3) Generate new table/spreadsheet with strict definition for easier data manip.
'''
#input: close value, date
#use: historical values (yesterday, last month, last quarter)
#output: Range of comparison values 
Input = 1
#Jan 20 2017 "the close on the day of the Trump Inauguration"
#D9475
Trump_Inaug = [20170120,23744.73,"the close on the day of the Trump Inauguration"]
float(1.00 - Input/Trump_Inaug[0])

#Nov 8 2016 "the close on the day of the 2016 Election"
#D9426
Election = [20161108,22165.78,"the close on the day of the 2016 Election"]
float(1.00 - Input/Election[0])

#Dec 15 2015 "the close before the Federal Reserve raised interest rates for the first time since June 29, 2006"
#D9199
Interest_raise = [20151215,21099.58,"the close before the Federal Reserve raised interest rates for the first time since June 29, 2006"]
float(1.00 - Input/Interest_raise[0])

#Sept 12 2012 "the close before Bernanke revealed QE3"
#D8380
QE3 = [20120912,15038.58,"the close before Bernanke revealed QE3"]
float(1.00 - Input/QE3[0])

#Aug 26 2010 "the close before Bernanke revealed QE2"
#D7864
QE2 = [20100826,10973.00,"the close before Bernanke revealed QE2"]
float(1.00 - Input/QE2[0])

#Mar 9 2009 "the financial Crisis low"
#D7493
crisis_low = [20090309,6858.43,"the Financial Crisis low"]
float(1.00 - Input/crisis_low[0])

#Oct 9 2007 "the old market high"
#D7138
old_market_high = [20071009,15806.69,"the old Market High"]
float(1.00 - Input/old_market_high[0])

def close_compare(close_value, operand_value):
	VAL_PERCENT = 1
	VAL_DOLLAR = 100
	return VAL_PERCENT, VAL_DOLLAR
	#Return (percentage change, money value difference)

def statement(VAL_DATE,VAL_PERCENT,VAL_DOLLAR):
	dat = lambda d: datetime.datetime.strptime(str(d),'%Y%m%d').strftime("%B %d, %Y")
	per = lambda p: "up " + str(p) if p >= 0 else "down " + str(p)
	dol = lambda y: str(float(y/1000.0)) + " trillion" if y >= 1000 else str(y) + " billion"
	print "Since " + dat(VAL_DATE) + ", the Wilshire 5000 is " + per(VAL_PERCENT) + " percent, or approximately $" + dol(VAL_DOLLAR)

'''
Day close
get_close_value()
Month-month end
datetime.datetime.strftime("%m")
Quarter-quarter end
if datetime.datetime.strftime("%m") % 3:
	pre-val = get [datetime.datetime.strftime("%m") - 3]

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
'''