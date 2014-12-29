import collections
import csv
from datetime import datetime
from bloomberg import Bloomberg
from ticker import Ticker
import operator

def main():
	bloomberg = Bloomberg()
	bloomberg.initializeData("exampleData.csv")

	print sorted(bloomberg.tickerObjects["SPX Index"].date_to_performance.items(), key=operator.itemgetter(0))
	# sorted(self.tickerObjects["SPX Index"].date_to_performance.items(), key=operator.itemgetter(0))

main()
