from audioop import ratecv
from PyTest import *
##//////////////////// PROBLEM STATEMENT ///////////////////
## Calculate how much money is earned by working a shift. //
## Read hours which contains the duration of the shift,   //
## rate which is the base amount of money earned per hour // 
## and bonus which is the HOURLY bonus earned on weekends // 
## or public holidays.                                    //
##                                                        //
##  hours rate bonus    result                            //
##    5     9    0   ->   45                              //
##    7    12    2   ->   98                              //
##//////////////////////////////////////////////////////////

hours = int(input('duration of the shift'))
rate = int(input('base amount of money ernned per hour'))
bonus = int(input('Hourly bonus earned on weekends'))

result = (hours*rate)+ (bonus*hours)
print(result)
