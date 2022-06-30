from PyTest import *
##///////////// PROBLEM STATEMENT /////////////
## Write Python code which, when it reads    // 
## two input boolean values, produces the    //
## following results:                        //
##                                           //
##   True True   -> False                    //
##   True False  -> False                    //
##   False True  -> False                    //
##   False False -> True                     //
##/////////////////////////////////////////////


a = input('Pls type a boolean: ').capitalize()
b = input('Pls type a boolean: ').capitalize()

if a and b == 'True':
    print('False')
elif a == 'True' and b == 'False':
    print('False')
elif a == 'False' and b == 'True':
    print('False')
else:
    print('True')
