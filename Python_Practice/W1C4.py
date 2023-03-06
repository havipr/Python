from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given 2 lists of ints, a and b, print True if they have the same first    //
## element or they have the same last element. Both lists will be length 1   //
## or more.                                                                  //
##    1, 2, 3    7, 3  -> True                                               //
##    1, 2, 3    7, 3, 2  -> False                                           //
##    1, 2, 3    1, 3  -> True                                               //
##/////////////////////////////////////////////////////////////////////////////



def same_first_last(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False
