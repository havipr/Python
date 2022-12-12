from PyTest import *
##/////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write a program which accepts a time interval in seconds and prints the //
## equivalent time in hours minutes seconds. One hour is 3600 seconds and  //
## one minute is 60 seconds.                                               //
##                                                                         //
##   Total seconds     hours  minutes  seconds                             //
##       3680       ->   1      10        20                               //       
##///////////////////////////////////////////////////////////////////////////

a = int(input('write the time in seconds: '))

time_in_hours = a//3600
left_minutes = a - time_in_hours 
time_in_minutes = left_minutes // 60
left_seconds = a - ((time_in_hours * 3600) + (time_in_minutes*60))
time_in_seconds = left_seconds



print(time_in_hours)
print(time_in_minutes)
print(time_in_seconds)
