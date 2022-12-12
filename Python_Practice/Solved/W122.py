from PyTest import *
from datetime import datetime
##/////////// PROBLEM STATEMENT ////////////////
## Given the time of day, in 24 hour format,  //
## print out the hour in 12 hr time.          //
##                                            //
##   eg 1330 = 1 o'clock, 2213 = 10 o'clock   //
##      1230 = 12 o'clock                     //
##                                            //
##   (Hint: Integer division will cut off     //
##    the value after the decimal completely. //
##     eg 18 // 10 = 1 and 18 / 10 = 1.8)     //
##//////////////////////////////////////////////

a = input("Write current time in 24 hour format: ")

name = a[0:2]
if name > 13:
    print(a // 10)
else:
    print(a)