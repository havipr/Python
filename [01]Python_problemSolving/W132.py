from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> True                     //
##   False False -> False                    //
##/////////////////////////////////////////////

a = input('Pls type a boolean: ').capitalize()
b = input('Pls type a boolean: ').capitalize()

if a and b == 'True':
    print('False')
elif a == 'True' & b == 'False':
    print('False')
#Why this line don't work
elif a == 'False' & b == 'True':
    print('True')
else:
    print('False')