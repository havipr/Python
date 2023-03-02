from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a list of ints, print True if the list contains a 2 next to a 2     //
## or a 4 next to a 4, but not both.                                         //
##    1, 2, 2  -> True                                                       //
##    4, 4, 1  -> True                                                       //
##    4, 4, 1, 2, 2  -> False                                                //
##/////////////////////////////////////////////////////////////////////////////


def prob1F3(nums):
    has_22 = False
    has_44 = False
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            has_22 = True
        elif nums[i] == 4 and nums[i+1] == 4:
            has_44 = True
    return has_22 != has_44
