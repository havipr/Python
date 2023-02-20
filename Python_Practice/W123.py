from PyTest import *
##//////////////////// PROBLEM STATEMENT ////////////////////////
## Given a 24 hour time of day as hours minutes seconds, add   //
## a time interval which is specified as hours minutes seconds //
##                                                             //
##   hrs mins secs hrs mins secs    hrs mins secs              // 
##   13   24   30   2   40   40  -> 16    5   10               //
##///////////////////////////////////////////////////////////////


from datetime import datetime, timedelta

#Input time
time_str = '13:24:30'
time = datetime.strptime(time_str, '%H:%M:%S')

#Input time interval
interval_str = '02:40:40'
hours, minutes, seconds = map(int, interval_str.split(':'))
interval = timedelta(hours=hours, minutes=minutes, seconds=seconds)

#Add interval to time
result = time + interval

#Print the result in the required format
print(result.strftime('%H %M %S'))
