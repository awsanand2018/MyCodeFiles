import datetime as dt
import pytz
mydt = dt.datetime(2018, 8, 19, 12, 10, 55, tzinfo=pytz.UTC)
print(mydt)
mytimezone=mydt.astimezone(pytz.timezone('US/Central'))