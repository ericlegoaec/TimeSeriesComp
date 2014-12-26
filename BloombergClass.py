# The purpose of this module is to be able to import data from Bloomberg into a format that will allow
# users to ascribe certain tickers to sets of time series data (both real total return, and performance).

from ticker import Ticker
import collections
import operator
import csv
from datetime import datetime

class Bloomberg:
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self):
        self.tickerNames = []
        self.tickerObjects = {}
            
    def initializeData(self, fileName):
            fileCopy = []

            # Printing out each row in order to show what is there
            with open(fileName) as csvfile:
                    reader = csv.reader(csvfile, delimiter = ",")
                    for row in reader:
                            fileCopy.append(row)

            csvfile.close()

            tickerNamesCounter = 0

            # Isolate the ticker names into the tickerNames list
            for x in fileCopy[0]:
                    if x == '':
                        pass
                    else:
                        self.tickerNames.append(x)

            print "The tickers that you have listed within your file include:"
            for x in self.tickerNames:
                print x

            # Associate performance data with each ticker via a dictionary
            # Dictionary will map datetime objects (for the date) to floats (for performance)

            # enumerate gives you an index value for each ticker in tickerNames, so we can know both
            #   the index and name of the ticker
            for index, ticker in enumerate(self.tickerNames):
                # a temporary map to hold a ticker's date/performance data
                performance_data_dict = {}

                # For each ticker, we go through the file checking the appropriate columns
                # You'll notice that corresponding columns of data for each ticker in the tickerNames list
                # is just 
                #   Date: 3*(index of ticker name in tickerNames)
                #   Performance: 3*(index of ticker name in tickerNames) + 1
                #
                # Math is a beautiful thing
                for line in fileCopy[2:]:
                    date_string = line[3*index]
                    if date_string == '':
                        continue
                    #create a datetime object out of the datestring in the csv file
                    date = datetime.strptime(date_string, '%m/%d/%Y')
                    performance = float(line[3*index + 1])

                    # add the date and performance to the dictionary
                    performance_data_dict[date] = performance

                # create a new ticker object, and store it in the tickerObjects dictionary which maps
                # ticker names (which are strings) to ticker objects (which are instances of the Ticker class)
                ticker_obj = Ticker(ticker, performance_data_dict)
                self.tickerObjects[ticker] = ticker_obj

            # note that the date_to_performance dictionary is not guaranteed to be sorted, so to sort it we can
            # use this line(which is the same thing used in the Ticker class
            print sorted(self.tickerObjects["SPX Index"].date_to_performance.items(), key=operator.itemgetter(0))
