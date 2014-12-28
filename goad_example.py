from BloombergClass import Bloomberg
import plotly.plotly as py
from plotly.graph_objs import *
import datetime

b = Bloomberg()
b.initializeData("exampleData.csv")

s_date = datetime.datetime(2014, 1, 31)
e_date = datetime.datetime(2014, 11, 28)
b.growthOfADollar("SPX Index", start_date=s_date, end_date = e_date)


