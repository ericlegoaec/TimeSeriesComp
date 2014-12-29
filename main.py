# As the main file, we must import the various classes and modules needed in order to run the program indefinitely.
import collections
import csv
from datetime import datetime
# <<<<<<< Updated upstream
from bloomberg import Bloomberg
from ticker import Ticker

def main():
        continueProgram = True
        bloomberg = Bloomberg()
        # What exactly does this line do?

	while continueProgram == True:
            print 'Welcome to the TimeSeriesComp program. Please choose from the menu below: ',
            print 'Select an option: \n1) Import data from Bloomberg \n2) Download data from Yahoo Finance API \n3) Quit'
            print ''
            userChoice = input("What would you like to do? ")
            if userChoice == 1:
                # Bloomberg data-scrub and push to next step
                #fileName = input('Please enter the name of the .csv file you would like to analyze: ')
                #print fileName
                
                launchBloombergMenu()
                break
                    
            elif userChoice == 2:
                # Yahoo API stuff
                pass
            else:
                continueProgram = False
                break

def launchBloombergMenu():

    print "Enter the path to the csv data file"
    print 'For example, if the file is called exampleData.csv, and it is located on your desktop,'
    print 'Type: ~/Desktop/exampleData.csv'

    data_file = raw_input()
    print data_file

    global bloomberg
    bloomberg = Bloomberg()

    bloomberg.initializeData(data_file)

    print 'Select an option:'
    print "1. Growth of a Dollar"
    print "2. Benchmarking"
    print "3. Exit"

    continueProgram = True

    while continueProgram == True:
        userChoice = input("What would you like to do? ")
        if userChoice == 1:
            launchGrowthMenu()
            break
                
        elif userChoice == 2:
            launchBenchmarkingMenu()
            break
        else:
            continueProgram = False
            break

def launchGrowthMenu():
    ticker_name = raw_input("Enter ticker name: ")
    starting_value = input("Enter starting value (i.e. 1000): ")
    s_date = raw_input("Enter start date (i.e 1/31/2013) or Press Enter to skip: ")
    if not s_date == "":
        s_date = datetime.strptime(s_date, "%m/%d/%Y")
    else:
        s_date = None

    e_date = raw_input("Enter end date (i.e 3/30/2014): ")
    if not e_date == "":
        e_date = datetime.strptime(e_date, "%m/%d/%Y")
    else:
        e_date = None

    plot_input = raw_input("Would you like to graph the data using plotly? (y/n): ")
    plot_it = None
    if plot_input == "y":
        plot_it = True
    else:
        plot_it = False

    print "Calculating..."
    bloomberg.growthOfADollar(ticker = ticker_name, start_value = starting_value, start_date = s_date, end_date = e_date, plot = plot_it)

def launchBenchmarkingMenu():
    
    b_marks = [bloomberg.tickerObjects[index] for index in bloomberg.tickerObjects.keys() if "Index" in index]
    tickers = [bloomberg.tickerObjects[ticker] for ticker in bloomberg.tickerObjects.keys() if "Index" not in ticker]

    bloomberg.benchmarking(b_marks, tickers)
                        
if __name__ == "__main__": main()
