from PyTest import *
##///////////////// PROBLEM STATEMENT ////////////////////
## Given an integer, print True if it is greater than   //
## zero and print False if it is not greater than zero. //
##   12 -> True                                         //
##   0  -> False                                        //
##   -8 -> False                                        //
##////////////////////////////////////////////////////////


a = int(input('Pls insert an integer: '))

if a >= 1:
    print('True')
else:
    print('False')