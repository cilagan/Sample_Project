import stocks
import datetime

print("*** Getting Stock Data ***")
print str(datetime.datetime.now())
print ""

print stocks.get_all("GOOG")

print "***"

print stocks.get_historical_prices("GOOG", "20131001", "20140529")

print("***")