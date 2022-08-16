from PyTest import *
##////////////// PROBLEM STATEMENT ////////////////
## We'll say that a number is "teen" if it is in //
## the range 13..19 inclusive. Given 3 integer   //
## values, print True if 1 or more of them are   //
## teen.                                         //
##   13, 20, 10 -> True                          //
##   20, 19, 10 -> True                          //
##   20, 10, 13 -> True                          //
##/////////////////////////////////////////////////

a = input('Pls write a 1: ')
b = input('Pls write a  2: ')
c = input('Pls write a 3: ')


if a >= '13' and a <= '19':
    print('True')
elif b >= '13' and b <= '19':
    print('True')
elif c >= '13' and c <= '19':
    print('True')
else:
    print('False')


# if any(x in a for x in range(13, 20)):
#     print('True')
# else:
#     print('False')