from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, print True if either of the strings appears at the     //
## very end of the other string, ignoring upper/lower case differences       //
## (in other words, the computation should not be "case sensitive").         //
##   "Hiabc", "abc" -> True                                                  //
##   "AbC", "HiaBc" -> True                                                  //
##   "abc", "abXabc" -> True                                                 //
##   "abc", "abXaXc" -> False                                                //
##/////////////////////////////////////////////////////////////////////////////

a = input('Insert a string').lower()
b = input('Insert a string').lower()
minChars = min(len(a), len(b))

# [start:end:step size]

mod_string_a = a[-minChars:]

# print(mod_string_a)
mod_string_b = b[-minChars::]
# print(mod_string_b)


if mod_string_a == mod_string_b:
    print('True')
else:
    print('False')

#How to check when there is just 2 letters?
