from PyTest import *
##/////////////// PROBLEM STATEMENT ////////////////
## Given two temperatures, print True if one is   //
## less than 0 and the other is greater than 100. //
##   120, -1 -> True                              //
##   -1, 120 -> True                              //
##   2, 120 -> False                              //
##//////////////////////////////////////////////////


a = input('Pls write a temperature: ')
b = input('Pls write another temperature: ')

def temperature(a,b):
    if a or b <= 0 and a or b >= 101: # Is this expresion correct?
        print('True') 
    else:
        print('False') 

temperature(a,b)
