from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Given two strings, append them together (known as "concatenation") and    //
## print the result. However, if the strings are different lengths, omit     //
## chars from the longer string so it is the same length as the shorter      //
## string. So "Hello" and "Hi" yield "loHi". The strings may be any length.  //
##                                                                           //
##   "Hello", "Hi" -> "loHi"                                                 //
##   "Hello", "java" -> "ellojava"                                           //
##   "java", "Hello" -> "javaello"                                           //
##/////////////////////////////////////////////////////////////////////////////

#Concatenate thogether
a = input('pls insert an input: ')
lsta = a.split()
b = input('pls insert an input: ')
lstb = b.split()
result = []




#Check the lenght of the string 
