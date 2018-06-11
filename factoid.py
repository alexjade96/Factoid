from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, \
	USMartinLutherKingJr, USPresidentsDay, GoodFriday, USMemorialDay, USLaborDay, \
<<<<<<< HEAD
	USThanksgivingDay, SU, MO, TU, WE, TH, FR, SA
from pandas.tseries.offsets import BDay, Day
from pandas import DateOffset
=======
	USThanksgivingDay
from pandas.tseries.offsets import BDay
>>>>>>> 1f750d97b5c0ff3c9c04bc9298882c938a8c86c5
from datetime import timedelta
import pandas as pd
import argparse
import datetime
<<<<<<< HEAD
import calendar
=======
>>>>>>> 1f750d97b5c0ff3c9c04bc9298882c938a8c86c5
import requests
import urllib2
import sys,os
import json
import time
import csv

#Create holiday calendar to deal with no market days
class WilshireHolidayCalendar(AbstractHolidayCalendar):
	rules = [
		Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
		USMartinLutherKingJr,
		USPresidentsDay,
		GoodFriday,
		USMemorialDay,
		Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
		USLaborDay,
		USThanksgivingDay,
<<<<<<< HEAD
		#Holiday('BlackFriday', month=11, day=1, offset=pd.DateOffset(weekday=FR(4))),
=======
>>>>>>> 1f750d97b5c0ff3c9c04bc9298882c938a8c86c5
		Holiday('Christmas', month=12, day=25, observance=nearest_workday)
	]

def append_line(df):
	test_insert = pd.DataFrame(df[-1:].values, index=[int(df.last_valid_index())+1], columns=df.columns)
	df = df.append(test_insert)
	print df.tail(2)

def adjust_dol(d):
	val = 1.00	#Default if (19771230 < d <= 19960628)
	if (19969628 < d <= 19990930) or (d > 20161231):
		val = 1.10
	if (19990930 < d <= 20000929) or (20090331 < d <= 20161231):
		val = 1.15
	if (20000929 < d <= 20040630) or (20071231 < d <= 20090331):
		val = 1.20
	if (20040630 < d <= 20071231):
		val = 1.25
	return val

def statement(VAL_DATE,DESC,VAL_PERCENT,VAL_DOLLAR):
	dat = lambda d: datetime.datetime.strptime(str(d),'%Y%m%d').strftime("%B %d, %Y")
	percent = lambda p: "up " + str(p) if p >= 0 else "down " + str(p)
	dollar = lambda y: str(abs(float(y/1000.0))) + " trillion" if abs(y) >= 1000 else str(abs(y)) + " billion"
	fact = "Since " + dat(VAL_DATE) + ", " + DESC + ", the Wilshire 5000 is " + percent(VAL_PERCENT) + " percent, or approximately $" + dollar(VAL_DOLLAR)
	return fact

def main(*args,**kwargs):
	#Function to get fiscal quarter month for a given datetime date object: VAR = quarter(datetime.datetime.today())
	today = datetime.datetime.today()
	quarter = lambda q: [q.strftime("%Y"+"%02d" % ((m-1)//3 + 1)+"01") for m in range(1,13) if "%02d" % m == q.strftime("%m")]
	q = quarter(datetime.datetime.now())[0]
	#print datetime.datetime.strptime(q,"%Y%m%d").weekday()
	#if quarter(today) not in 

	specs = [
		int(datetime.datetime.now().strftime("%Y%m%d")),
		int((pd.datetime.today() - BDay(1)).strftime("%Y%m%d")),
		int((pd.datetime.today() - BDay(2)).strftime("%Y%m%d")),
		int(datetime.datetime.now().strftime("%Y%m01")),
		int(datetime.datetime.now().strftime("%Y%m02")),
		int(datetime.datetime.now().strftime("%Y0102")),
		int(quarter(datetime.datetime.now())[0]),
		20180221,
		20180220,
		20180219,
		20180126,
		20170120,
		20161108,
		20160211,
		20151215,
		20120912,
		20100826,
		20090309,
		20071009
	]

	milestones = {
		int((pd.datetime.today() - BDay(1)).strftime("%Y%m%d")):"the last close",
		int((pd.datetime.today() - BDay(2)).strftime("%Y%m%d")):"the last close",
		int(datetime.datetime.now().strftime("%Y%m01")):"for the month",
		int(datetime.datetime.now().strftime("%Y%m02")):"for the month",
		int(datetime.datetime.now().strftime("%Y0102")):"for the year",
		int(quarter(datetime.datetime.now())[0]):"for the quarter",
		20170120:"the close on the day of the Trump Inauguration",
		20161108:"the close on the day of the 2016 Election",
		20151215:"the close before the Federal Reserve raised interest rates for the first time since June 29, 2006",
		20120912:"the close before Bernanke revealed QE3",
		20100826:"the close before Bernanke revealed QE2",
		20090309:"the Financial Crisis low",
		20071009:"the old Market High"
	}

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
	outdir = "out"
	outfile = "factoid_"+datetime.datetime.now().strftime("%Y%m%d")+".txt"
	out = open(outfile,'w')

	xl = pd.ExcelFile(xl_file)
	xl.sheet_names
	df = xl.parse(sheet1)
	compare = df[df.iloc[:,0].isin(specs)].iloc[:,[0,3]]

	chosen_date = pd.datetime.today()
	cur_df = df[df['Wilshire 5000 (Full Cap) Price'] == int(chosen_date.strftime("%Y%m%d"))]#.iloc[:,[0,3]]
	while cur_df.empty:
		chosen_date = chosen_date - BDay(1)
		cur_df = df[df['Wilshire 5000 (Full Cap) Price'] == int(chosen_date.strftime("%Y%m%d"))]
	out.write("Most recent date from file: "+chosen_date.strftime("%Y%m%d")+"\n")
	index = cur_df.index[0]
	print index
	print df.iloc[index-1,0:3]
	cur_close = int(cur_df.iloc[:,0])
	cur_val = float(cur_df.iloc[:,3])
	print "cur",cur_close,cur_val
	print df.tail(2).head(1).iloc[:,[0,3]]
	print compare
	#Start Comparison

	outlist = []

	for index, row in compare.iterrows():
		if int(row[0]) in milestones:
			d = int(row[0])
			desc = milestones[int(row[0])]
			pre_val = float(row[1])
			points = round((cur_val - pre_val),-2)
			perc = round(float(cur_val/pre_val - 1)*100.00,2)
			diff = (cur_val - pre_val)
			multiplier = float(adjust_dol(d))
			dol = round(float(diff*multiplier),-2)
			if (diff*multiplier) < 1000:
				dol = round(float(dol * 4),-2)
				
			print "=====",d,pre_val,cur_val,diff,perc,multiplier,dol,points,"====="
			data = statement(d,desc,perc,dol)
			print data
			if data not in outlist:
				outlist.append(data)

	for item in outlist:
		print item
		out.write(item+"\n")
	out.close()
	"""
	========================
	Logic for dollar values:
	========================
	All of the values AFTER 20170120 (so basically the dollar values in AM, AI, AG, AE, AB, Y,F), are the below formula:
	=IF(VALUE*1.1<1000,(ROUND(4*(VALUE*1.1),-2)/4),(ROUND(VALUE*1.1,-2)))
	if d > 20170120:

	Then for 20161108, 20151215, 20120912, 20100826 (AO,AQ,AS,AU) the formula is:
	=IF(VALUE*1.15<1000,(ROUND(4*(VALUE*1.15),-2)/4),(ROUND(VALUE*1.15,-2)))
	if d > 20100120:

	Then for 20090309 (AW), the formula is:
	=IF(VALUE*1.2<1000,(ROUND(4*(VALUE*1.2),-2)/4),(ROUND(VALUE*1.2,-2)))
	if d > 20080120:

	Finally for 20071009 (BK), the formula is:
	=IF(VALUE*1.25<1000,(ROUND(4*(VALUE*1.25),-2)/4),(ROUND(VALUE*1.25,-2)))
	else: #Date  is 20071009
		
	"""


	#append_line(df)

	#print df.tail(22)
	#df.dropna(thresh=2)
	#print df.tail(22)
	#print df[9715:9721]
	#print df[:-22].dropna(thresh=2)
	#Use [Max - 27] to get latest Date
	#yesterday = df.tail(1)

	#for item in specs:
		#print df['Wilshire 5000 (Full Cap) Price'].str.contains(item)#.isin(comparisons)
	#print df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)]

	#for i in range(0,temp.shape[0]):
		#for j in range(0,temp.shape[1]):
			#print "("+str(i)+","+str(j)+")",df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)].iloc[i,j]
	'''
	#Get range of columns
	temp = df[df['Wilshire 5000 (Full Cap) Price'].isin(specs)].iloc[:,0:4]
	print "temp",temp
	#Get all items listed from specs
	test = df[df.iloc[:,0].isin(specs)].iloc[:,[0,3]]
	print "test",test
	#Get spec item + close value
	current = df.tail(1).iloc[:,[0,3]]
	print "current",current
	#Get pure value
	val = float(df.tail(1).iloc[:,3])
	print "val",val
	#Get pure date/val info
	info = test.to_csv(header=None,index=False)
	print "info",info

	for index, row in test.iterrows():
		print row[0],row[1]
	'''
	#for item in info:
	#	print type(item),item
		#blah = df.iloc[item:,[0,3]]
		#print "blah",blah
	#for n in range(0,test.shape[0]):
		#print type(test.iloc[n,0]),test.iloc[n,0],type(test.iloc[n,1]),test.iloc[n,1]

	#Need Date, Value
	#Calculate percentage, difference, dollar amount, dollar difference
	#Store as lists?
	Trump_Inaug,Election,Int_Raise,QE2,QE3,Crisis_Low,Old_High,= ([] for i in range(7))

	'''
	1) Define & use formulas outside of xlsx worksheet/inside script
	2) Use COM/win32 to use existing Excel formulas (win dev only)
	3) Generate new table/spreadsheet with strict definition for easier data manip.
	'''
	#val: close value, date
	#use: historical values (yesterday, last month, last quarter)
	#output: Range of comparison values 
	val = 1
	#Jan 20 2017 "the close on the day of the Trump Inauguration"
	#D9475
	Trump_Inaug = [20170120,23744.73,"the close on the day of the Trump Inauguration"]
	float(1.00 - val/Trump_Inaug[0])

	#Nov 8 2016 "the close on the day of the 2016 Election"
	#D9426
	Election = [20161108,22165.78,"the close on the day of the 2016 Election"]
	float(1.00 - val/Election[0])

	#Dec 15 2015 "the close before the Federal Reserve raised interest rates for the first time since June 29, 2006"
	#D9199
	Interest_raise = [20151215,21099.58,"the close before the Federal Reserve raised interest rates for the first time since June 29, 2006"]
	float(1.00 - val/Interest_raise[0])

	#Sept 12 2012 "the close before Bernanke revealed QE3"
	#D8380
	QE3 = [20120912,15038.58,"the close before Bernanke revealed QE3"]
	float(1.00 - val/QE3[0])

	#Aug 26 2010 "the close before Bernanke revealed QE2"
	#D7864
	QE2 = [20100826,10973.00,"the close before Bernanke revealed QE2"]
	float(1.00 - val/QE2[0])

	#Mar 9 2009 "the financial Crisis low"
	#D7493
	crisis_low = [20090309,6858.43,"the Financial Crisis low"]
	float(1.00 - val/crisis_low[0])

	#Oct 9 2007 "the old market high"
	#D7138
	old_market_high = [20071009,15806.69,"the old Market High"]
	float(1.00 - val/old_market_high[0])

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

if __name__ == '__main__':
	main()
