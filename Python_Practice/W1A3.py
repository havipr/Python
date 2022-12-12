from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string.                                                      //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////


word = input('type the word: ')
countCat = 0
countDog = 0

for i in range(len(word) - 2):
    if word[i] == 'c':
        if word[i+1] == 'a':
            if word[i+2] == 't':
                countCat += 1

for j in range(len(word) - 2):
    if word[j] == 'd':
        if word[j+1] == 'o':
            if word[j+2] == 'g':
                countDog += 1


if countCat == countDog:
    print(True)
else:
    print(False)

    