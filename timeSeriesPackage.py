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

# All available dates
dates1 = []
dates2 = []

# Dictionaries
dateToValue1 = {}
dateToValue2 = {}

# Start reading in dates from 2nd row on
for x in fileCopy[2:]:
        if(x[0] != ''):
            date_1 = datetime.strptime(x[0], '%m/%d/%Y')
	    dates1.append(date_1)
            dateToValue1[date_1.strftime('%m-%d-%Y')] = x[1]
        if(x[3] != ''):    
            date_2 = datetime.strptime(x[3], '%m/%d/%Y')
	    dates2.append(date_2)
	    dateToValue2[date_2.strftime('%m-%d-%Y')] = x[4]

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

# print valueIndexList
print valueIndexList
# At this time, we need to create the first dictionary to pair with the value from each date
for valueIndex in valueIndexList:
	# ~~~~~~~~~~~~~~~~~~~~~~~
	# PROBLEM CODE
	# ~~~~~~~~~~~~~~~~~~~~~~~
	for line in fileCopy[2:]:
		tickerValue = line[valueIndex]
		tempValueList.append(tickerValue)
		# The templist is going through all the values. We need to either wipe the tempList after
		# or determine how to increment through.

	# ~~~~~~~~~~~~~~~~~~~~~~~
	# PROBLEM CODE
	# ~~~~~~~~~~~~~~~~~~~~~~~

	listOfLists_ofValues.append(list(tempValueList))
	del tempValueList[:]
	
print listOfLists_ofValues

# for x in listOfLists_ofValues:
# 	print x
# 	print

# Create the first dictionary
tickerDictionary = {}
tempDict = {}
timeSeriesIndex = 0
valueIndex = 0
listIndex = 0


if len(listOfLists_ofDates) == len(listOfLists_ofValues):
	for ticker in tickerNames:
		for timeSeries in listOfLists_ofDates:
			for date in timeSeries:
				tempDict[date] = listOfLists_ofValues[timeSeriesIndex][valueIndex]
				valueIndex += 1

			timeSeriesIndex += 1

		tickerDictionary[ticker] = tempDict

print tickerDictionary
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Check to make sure that everything works
# print dates1,
# print ""
#print dates2,

# TODO: Find the earliest overlapping date between the two sets of lists
if dates1[0] < dates2[0]:
    #The first date in the dates1 list is earlier than the other, so earliest overlapping
    #   date must be dates2 first value
    #   This is of course assuming Bloomberg data is complete for each date
    earliest_date = dates2[0].strftime('%m-%d-%Y')
else:
    earliest_date = dates1[0].strftime('%m-%d-%Y')

# print "earliest date: " + str(earliest_date)
# TODO: Objective 1: isolate the dates and values for each of the corresponding lists
# *Remember that each list has its own set of values, and is independent
#  from any other list.
