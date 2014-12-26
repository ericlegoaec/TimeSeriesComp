import collections
from datetime import datetime
from datetime import timedelta
import csv

fileCopy = []

# Printing out each row in order to show what is there
with open("exampleData.csv") as csvfile:
	reader = csv.reader(csvfile, delimiter = ",")
	for row in reader:
		fileCopy.append(row)

csvfile.close()

# print fileCopy

tickerNames = []
tickerNamesCounter = 0


# Isolate the ticker names into the tickerNames list
for x in fileCopy[0]:
	if x == '':
	    pass
	else:
	    tickerNames.append(x)

# Verify that ticker names are transferred to the list
# print tickerNames

# Pair dates and ticker names into a double dictionary structure
indexCounterStart = 2
valueCounter = 0

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Edit: Jameson
# Attempt to try to create a list of lists in order to scale recording of values
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 # Create a 'list of lists'
listOfLists_ofDates = []
listOfLists_ofValues = []

# Create initial starting point for listOfLists
indexFromTickerNames = []
NAMES = len(tickerNames)
initial_start = 0
# print NAMES

for x in range(0,NAMES):
    if x > 0:
        initial_start += 2
        indexFromTickerNames.append(initial_start + 1)
    else:
        indexFromTickerNames.append(x)
# Proof of concept 'print' to show that number of tickers impacts the list range
# print indexFromTickerNames

# We know that data is organized in the following way:
# [date] [value] [space] [date] [value]
# Therefore, we can create automatic lists given this information
tempList = []
tempListNameIndex = 0
for x in indexFromTickerNames:
	for i in fileCopy[2:]:
		if i != '':
			tickerDate = i[x]
			tempList.append(tickerDate)
		else:
			pass

	listOfLists_ofDates.append(list(tempList))
	del tempList[:]

# It works!!!
# for x in listOfLists_ofDates:
# 	print x
# 	print

tempValueList = []
valueIndexList = []

for value in indexFromTickerNames:
	valueIndexList.append(value + 1)


# At this time, we need to create the first dictionary to pair with the value from each date
for valueIndex in valueIndexList:

	for line in fileCopy[2:]:
		if line != '':
			tickerValue = line[valueIndex]
			tempValueList.append(tickerValue)
		else:
			pass

	listOfLists_ofValues.append(list(tempValueList))
	del tempValueList[:]
	
# print listOfLists_ofValues

# for x in listOfLists_ofValues:
# 	print x
# 	print

# Create the first dictionary
tickerDictionary = {}
tempDict = {}
# Need to pull the number of values within each individual list, not the full
timeSeriesIndex = 0

# Find indices in the dates value:
for line_list in listOfLists_ofDates:
	for date in line_list:
		timeSeriesIndex += 1


IndividualTickerDictionary_LENGTH = (timeSeriesIndex / len(tickerNames))

LOL_Values_List_Iterator = 0
valueIndex = 0
listIndex = len(listOfLists_ofDates)

# Create the double dictionary structure
for ticker in tickerNames:
	for listRange in range(0,listIndex):
		for dateRange in range(0,IndividualTickerDictionary_LENGTH):
			tempDict[listOfLists_ofDates[listRange][dateRange]] = listOfLists_ofValues[listRange][dateRange]

	tickerDictionary[ticker] = tempDict

# # Test:
# for x in tickerDictionary['LYV US Equity']:
# 	print x
# 	print

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: PerformanceCalculator
# Inputs: Double Dictionary of (ticker : dictionary(date : values)), original lists of dates - LOL_Dates
# Description: Calculate performance for all 
# Outputs: LOL_ReturnData
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
performance_DD = collections.OrderedDict()
temp_Performance_DD = collections.OrderedDict()

for ticker in tickerNames:
	for listRange in range(0, listIndex):
		for date in range(0, len(listOfLists_ofDates[listRange])):
			if date <= len(listOfLists_ofDates[listRange])-2:
				
				if (tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date + 1])) != '':
					T_1value = float((tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date + 1])))
				else:
					pass

				if (tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date])) != '':
					T_0value = float((tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date])))
				else:
					pass

				date_per_ticker = listOfLists_ofDates[listRange][date]

				temp_Performance_DD[date_per_ticker] = ((T_1value / T_0value) - 1)
			else:
				pass

	performance_DD[ticker] = temp_Performance_DD

print performance_DD


# Calculates the earliest date (forward an additional date for performance calculations)
# def getEarliestDate():
#     earliest_date = getCommonDate()
#     earliest_date += timedelta(days=1)
#     return earliest_date
# 
# ***Jameson Edit***
# This is incorrect because the earliest date of one security may or may not begin before or 
# after the common date between 2 or more securities / indeces.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: EarliestDate_Performance
# Inputs: LOL_Dates
# Description: Finds the earliest date where performance data can be listed
# Outputs: List of earliest_dates
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# EarliestDate_Performance = {}
# for ticker in performance_DD:
# 	for date in 
# 		EarliestDate_Performance[ticker] = 

# print EarliestDate_Performance



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function: CommonDate_Performance
# Inputs: LOL_Dates
# Description: Finds the earliest common date where performance data can be listed between 2 or more securities
# Outputs: 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 
# Calculates the earliest common date
# def getCommonDate():
    # common_date = datetime.strptime(listOfLists_ofDates[0][0], '%m/%d/%Y')
# This requires a double For-loop, not a single for-loop
# 
#     for ticker in range(1, len(listOfLists_ofDates)):
#         first_date = datetime.strptime(listOfLists_ofDates[ticker][0], '%m/%d/%Y')
#         if first_date > common_date:
#             common_date = first_date

#     return common_date