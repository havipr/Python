from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## We'll say that a "nsequence" in a string is a char appearing n times in   //
## a row. Given a string and an integer n, print the number of nsequences in //
## the given string. The nsequences may overlap. Use a function to count the //
## number of nsequences.                                                     //
##   "abcXXXabc" 3 -> 1                                                      //
##   "xxxabyyyycd" 3 -> 3                                                    //
##   "a" 2 -> 0                                                              //
##/////////////////////////////////////////////////////////////////////////////


def count_nsequences(string, n):
    count = 0
    for i in range(len(string)-n+1):
        if string[i:i+n] == string[i]*n:
            count += 1
    return count

# Example usage:
print(count_nsequences("abcXXXabc", 3))   
print(count_nsequences("xxxabyyyycd", 3)) 
print(count_nsequences("a", 2))          
