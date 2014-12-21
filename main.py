# As the main file, we must import the various classes and modules needed in order to run the program indefinitely.
import collections
import csv
from datetime import datetime
import BloombergClass.py

continueProgram = True
def main():
	while continueProgram == True:
		print 'Welcome to the TimeSeriesComp program. Please choose from the menu below: '
		print 'Select an option: \n1) Import data from Bloomberg \n2) Download data from Yahoo Finance API \n3) Quit'
		print ''
		userChoice = input("What would you like to do?")

		if userChoice == 1:
			# Bloomberg data-scrub and push to next step
			fileName = input('Please enter the name of the .csv file you would like to analyze: ')
			fileCopy = downloadData(fileName)
			
		elif userChoice == 2:
			# Yahoo API stuff
			pass
		else:
			continueProgram = False
			break