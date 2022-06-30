from PyTest import *
##/////////////////////////// PROBLEM STATEMENT /////////////////////////
## Write a program which accepts a time interval in hours, minutes and //
## seconds and prints the equivalent time in just seconds. One hour is //
## 3600 seconds and one minute is 60 seconds.                          //
##                                                                     //
##   hours  minutes  seconds     Total seconds                         //
##     1       10       20    ->    4220                              //
##///////////////////////////////////////////////////////////////////////


a = int(input('pls insert a time in hours: '))
b = int(input('pls insert a time in minutes: '))
c = int(input('pls insert a time in seconds: '))

seconds_in_hour = 3600
seconds_in_minutes = 60

hour_in_seconds = a*seconds_in_hour
minutes_in_seconds = b*seconds_in_minutes

print(hour_in_seconds+minutes_in_seconds+c)