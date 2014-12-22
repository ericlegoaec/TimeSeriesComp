import collections
from datetime import datetime
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
		tickerDate = i[x]
                if not tickerDate == '':
		    tempList.append(tickerDate)

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
	# ~~~~~~~~~~~~~~~~~~~~~~~
	# PROBLEM CODE
	# ~~~~~~~~~~~~~~~~~~~~~~~
	for line in fileCopy[2:]:
		tickerValue = line[valueIndex]
                if not tickerValue == '':
		    tempValueList.append(tickerValue)
		# The templist is going through all the values. We need to either wipe the tempList after
		# or determine how to increment through.

	# ~~~~~~~~~~~~~~~~~~~~~~~
	# PROBLEM CODE
	# ~~~~~~~~~~~~~~~~~~~~~~~

	listOfLists_ofValues.append(list(tempValueList))
	del tempValueList[:]
	
# print listOfLists_ofValues

# for x in listOfLists_ofValues:
# 	print x
# 	print

# Create the first dictionary
tickerDictionary = collections.OrderedDict()
tempDict = collections.OrderedDict()
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

# Test:
# print tickerDictionar

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
				# Need to get the computer to read values as ints, and not strings
				# Obviously, this would not be the calculation used to determine performance....
                                print (tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date + 1]))
				#temp_Performance_DD[listOfLists_ofDates[listRange][date]] = (float((tickerDictionary.get(ticker).get(listOfLists_ofDates[listRange][date + 1]))) / 10000)
                                
	
			else:
				pass

	performance_DD[ticker] = temp_Performance_DD

print performance_DD

# print tickerDictionary['SPX Index']['1/31/1990']




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description: Find the earliest overlapping date between all available date ranges
# Function: EarliestDate
# Inputs: 
# Description: 
# Outputs: 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# TODO: Find the earliest overlapping date between the two sets of lists
# if dates1[0] < dates2[0]:
#     #The first date in the dates1 list is earlier than the other, so earliest overlapping
#     #   date must be dates2 first value
#     #   This is of course assuming Bloomberg data is complete for each date
#     earliest_date = dates2[0].strftime('%m-%d-%Y')
# else:
#     earliest_date = dates1[0].strftime('%m-%d-%Y')
