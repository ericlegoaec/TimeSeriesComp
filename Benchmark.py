# Benchmark.py
# Purpose: Create the methodology for comparing the real total returns of a benchmark in excess
# 		   of specified benchmarks.

from BloombergClass import BloombergClass
from ticker import Ticker


class Benchmark:

	# This will be composed of the tickerObjects created in the BloombergClass module
	def __init__(self, bloombergClassData):
		tObjects_ListOfBenchmarks = []
		tObjects_ListOfSecurities = []

		for x in bloombergClassData:
			if x[-5] == 'Index':
				# Append to the benchmark list
				tObjects_ListOfBenchmarks.append(x)
			else:
				# Append to the securities list
				tObjects_ListOfSecurities.append(x)

		self.number_of_benchmarks = 0
		self.number_of_securities = 0
		
		for benchmark in tObjects_ListOfBenchmarks:
			self.number_of_benchmarks += 1

		for security in tObjects_ListOfSecurities:
			self.number_of_securities += 1

		print 'There are a total of ' + self.number_of_benchmarks + ' being compared to ' +
			  '\n'self.number_of_securities + ' securities. \n'

	def commonDateFinder(tickerObjects):
		common_date = None

		for ticker in tickerObjects:
			if ticker.earliest_date > common_date:
				common_date = earliest_date

		return common_date

	def benchmarkingAnalysis(tickerObjects, common_date):
		commonDate = commonDateFinder(tickerObjects)

		

			
	

