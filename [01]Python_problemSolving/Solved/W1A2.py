from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print True if "bad" appears starting at index 0 or 1 in   //
## the string, such as with "badxxx" or  "xbadxx" but not "xxbadxx". The     //
## string may be any length, including 0.                                    //
##   "badxx" -> True                                                         //
##   "xbadxx" -> True                                                        //
##   "xxbadxx" -> False                                                      //
##/////////////////////////////////////////////////////////////////////////////

#Ask for user input 
a = input('pls type a word: ').lower()
#convert the input into a list 
lst = a.split()

#iterate the list 
for i in lst:
    #We slice it to check the first 3 characters
    if i[0:3] == 'bad':
        print(True)
    #We slice it to check the first 3 characters
    elif i[1:4] == 'bad':
        print(True)
    #if none are True print False 
    else:
        print(False)