import datetime 
import pytz
mydt=datetime.datetime.now(tz=pytz.UTC) # To convert it into UTC timezone
print(mydt)
est_time=mydt.astimezone(pytz.timezone('US/Eastern'))
print(est_time)
date_to_string=est_time.strftime('%B %d, %Y') # String Format Time. Converts date/time into string. The output is a string now.
print(date_to_string)
string_to_date=datetime.datetime.strptime(date_to_string,'%B %d, %Y') # String Parse Time.This method takes two args. One arg is the string that contains date as string and another arg is the format. This method converts the string to date/time format.
print(string_to_date)
print(string_to_date.date()) # To extract only the date from the output