import urllib2, urllib, json

baseurl = "https://query.yahooapis.com/v1/public/yql?"
yql_query = 'select * from yahoo.finance.historical where symbol = "YHOO"'
#yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
yql_url = "https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.historicaldata%20where%20symbol%20%3D%20%22{}%22%20and%20startDate%20%3D%20%222014-01-01%22%20and%20endDate%20%3D%20%222014-12-18%22&format=json&diagnostics=true&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys&callback=".format("AAPL")
result = urllib2.urlopen(yql_url).read()
data = json.loads(result)

for quote in data['query']['results']['quote']:
    print quote["High"]
