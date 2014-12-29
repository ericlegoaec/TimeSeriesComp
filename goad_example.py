from bloomberg import Bloomberg
import plotly.plotly as py
from plotly.graph_objs import *
import datetime

b = Bloomberg()
b.initializeData("exampleData.csv")

s_date = datetime.datetime(year=2014, month=1, day=12)
e_date = datetime.datetime(2014, 11, 28)

b.growthOfADollar("SPX Index", plot=False, start_date=s_date, end_date = e_date)

benchmark = [b.tickerObjects["SPX Index"]]
comparison_ticker = [b.tickerObjects["LYV US Equity"]]

b.benchmarking(benchmark, comparison_ticker)
