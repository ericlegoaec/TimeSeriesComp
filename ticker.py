# This class will be used in order to create the Ticker Class.
# Here, we will store Ticker member variables, which will be used in the construction of double dictionary structures.
# We must also import the relevant modules.

import os
import operator
from datetime import datetime

class Ticker:

        # Constructor: creates ticker object with associate performance data 
        # Assumes date_to_performance is a dictionary where
        #   Key: datetime object (for the corresponding date)
        #   Value: float (performance data)
        # Using datetime as the dictionary key is convenient because it allows easy comparison of date values
        def __init__(self, ticker, date_to_performance):
            
            # String for the ticker
            self.ticker = ticker
            
            # instance variable for dictionary from date to performance
            self.date_to_performance = date_to_performance

            # Since date_to_performance is a dictionary of datetime objects to floats,
            #   sort the dictionary by the datetime value 
            #   (note that the key=operator.itemgetter(0) bit tells the sorted() method to sort based on the dictionary's key,
            #   in this case datetime)
            #   The sorted method creates a list of tuples in the form: [(datetime1, performance1), (datetime2, performance2)...]
            #   For sorted(date_to_performance.items(), key=operator.itemgetter(0))[1][0], the [1] part grabs the second tuple
            #       (i.e. the tuple at the first index) and the [0] part grabs the first part of that tuple (i.e. the datetime value)
            # whew...
            self.earliest_date = sorted(date_to_performance.items(), key=operator.itemgetter(0))[1][0]

        # Just a convenient method to get performance for a date (might be overkill, but what the hell)
        def getPerformanceForDate(self, datetime)

            return date_to_performance[datetime]
