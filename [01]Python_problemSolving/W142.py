from PyTest import *
##////////////////////////////// PROBLEM STATEMENT /////////////////////////////
## Write Python code that reads two integers from the keyboard.               //
## If the first integer is in the range 1. . 100 and the first integer is     //
## less than the second integer OR if the first integer is at least twice     //
## the second integer and the second integer is not in the range -8..16       //
## (with the exception it can be zero) print True. Otherwise print False.     //
## You must not use the Python if or if-else statement.                       //
##                                                                            //
## All ranges are inclusive                                                   //
##                                                                            //
## Example inputs/outputs are:                                                //
##    10 50   -> True                                                         //
##    20 5    -> False                                                        //
##    100 20  -> True                                                         //
##    30 20   -> False                                                        //
##    2 0     -> True                                                         //
##    16 -5   -> False                                                        //
##//////////////////////////////////////////////////////////////////////////////

a = int(input('Pls write the first integer: '))
b = int(input('Pls write the second integer: '))

c = False 

while (a < b and a in range(1, 101)) or (a >= (b*2) and (b not in range(-8, 17) or b == 0)):
    c = True
    break
print(c)
