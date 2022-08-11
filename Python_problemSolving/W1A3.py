from PyTest import *
##//////////////////////////// PROBLEM STATEMENT //////////////////////////////
## Print True if the string "cat" and "dog" appear the same number of times  //
## in the given string.                                                      //
##   "catdog" -> True                                                        //
##   "catcat" -> False                                                       //
##   "1cat1cadodog" -> True                                                  //
##/////////////////////////////////////////////////////////////////////////////

word = input('type the word: ')
countCat = []
countDog = []

while True:
    cat = word[:3]
    if cat == 'cat':
        countCat.append(cat)
    dog = word[3:]
    if dog == 'dog':
        countDog.append(dog)
    break


if countCat == countDog:
    print(True)

    