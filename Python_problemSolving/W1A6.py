from operator import ne
from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given a string, print a version without the first 2 chars. Except keep    //
## the first char if it is 'a' and keep  the second char if it is 'b'. The   //
## string may be any length.                                                 //
##   "Hello" -> "llo"                                                        //
##   "java" -> "va"                                                          //
##   "away" -> "aay"                                                         //
##/////////////////////////////////////////////////////////////////////////////

#We ask the user for an input 
a = input('Pls insert an input: ')

#We convert the input into a list to check each item 
newa = a.split()

#iterate the len of the list 
for i in range(len(newa)):
    #if the first caracter is a
    if newa[0][0] == 'a':
        print(newa[0][0], newa[0][2:])
    #if the second caracter is b   
    elif newa[0][0] == 'b':
        print(newa[1],newa[0][2:])
    #if the input dosent have any a or b at in the index 0 
    else:
        print(newa[0][2:])

