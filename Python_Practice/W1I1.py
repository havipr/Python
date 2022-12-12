from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if every element is a 1 or a 4.          //
##    1, 4, 1, 4  -> True                                                    //
##    1, 4, 2, 4  -> False                                                   //
##    1, 1  -> True                                                          //
##/////////////////////////////////////////////////////////////////////////////

a = (input('Type some numbers: '))

for i in a:
    if i == "1" or "4":
        print(True)
    else:
        print(False)