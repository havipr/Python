from PyTest import *
##/////////// PROBLEM STATEMENT ///////////////
## Given 2 int values, print True if either  //
## of them is in the range 10..20 inclusive. //
##   12, 99 -> True                          //
##   21, 12 -> True                          //
##   8, 99 -> False                          //
##/////////////////////////////////////////////

a = int(input('number: '))
b = int(input('number: '))

if a in range(10, 21) or b in range(10, 21): 
    print('True')
else:
    print('False')