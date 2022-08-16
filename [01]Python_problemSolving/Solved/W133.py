from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> True                     //
##   True False  -> False                    //
##   False True  -> False                    //
##   False False -> True                     //
##/////////////////////////////////////////////

a = input('Pls type a boolean: ').capitalize()
b = input('Pls type a boolean: ').capitalize()

if a and b == 'True':
    print('True')
elif a == 'True' and b == 'False':
    print('False')
#Why this line don't work?
elif a == 'False' and b == 'True':
    print('False')
else:
    print('True')