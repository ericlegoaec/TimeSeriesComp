# The purpose of this module is to be able to import data from Bloomberg into a format that will allow
# users to ascribe certain tickers to sets of time series data (both real total return, and performance).

from ticker import Ticker
import collections
import operator
import csv
from datetime import datetime

import plotly.plotly as py
from plotly.graph_objs import *


class Bloomberg:
    """Provides growth and benchmarking calculations for ticker performance data.
    """
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def __init__(self):
        self.tickerNames = []
        self.tickerObjects = {}
            
    def initializeData(self, fileName):
        """Loads and initializes data from a csv file.

        Args:
            filename: The csv data file
        """

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
        # use this line (which is the same thing used in the Ticker class)
        # print sorted(self.tickerObjects["SPX Index"].date_to_performance.items(), key=operator.itemgetter(0))

    def growthOfADollar(self, ticker, start_value=1000, start_date=None, end_date=None, plot=False):
        """Calculates the growth of a dollar of a range of time.

        Requires a ticker string to calculate growth, and defaults to calculating the growth of $1000
        over the entirety of return data provided in the csv data file.

        Args:
            ticker (str): The ticker string used to calculate growth
            start_value (int): Initial dollar ammount
            start_date (datetime): Starting date for range of time
            end_date (datetime): Ending date
            plot (bool): Graph the growth data in a plotly graph

        """
        # Sort performance data
        performance_data = sorted(self.tickerObjects[ticker].date_to_performance.items(), key=operator.itemgetter(0))
        
        
        if start_date is None:
            start_date = performance_data[0][0]
            
        if end_date is None:
            # Set date range over entire period
            end_date = performance_data[-1][0]

        # value_over_time holds sequence of monthly total values
        self.value_over_time = [start_value]

        # Retrieve start and end indexes for the time series date range
        #   Uses index() to match index of a tuple (month, year) for start and end date values.
        #   We compare tuples of month and year since we don't care about a 
        #       datetime's `day` value in making the index() comparison
        start_index = [(x[0].month, x[0].year) for x in performance_data].index((start_date.month, start_date.year)) + 1
        end_index = [(x[0].month, x[0].year) for x in performance_data].index((end_date.month, end_date.year))

        for index, month_data in enumerate(performance_data[start_index:end_index]):
            current_index = start_index + index
            past_month_value = performance_data[current_index-1][1]
            current_month_value = performance_data[current_index][1]

            growth_value = self.value_over_time[-1] # Last value in the growth time series

            month_return = ((current_month_value/past_month_value)-1) # Calculate return
            
            new_value = growth_value + growth_value * month_return # Apply return to dollar value
            self.value_over_time.append(new_value)

        print self.value_over_time[-1]

        # Create graph using Plotly
        if plot:
            py.sign_in("jpugliesi", "ul7hpg2obk")
            
            trace1 = Scatter(
               x = [x[0] for x in performance_data[start_index-1:end_index]],
               y = self.value_over_time
            )

            data = Data([trace1])
            plot_url = py.plot(data, filename='basic-line')

        return self.value_over_time


