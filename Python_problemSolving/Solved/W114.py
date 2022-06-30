from PyTest import *
##/////////////// PROBLEM STATEMENT /////////////////
## Convert a height input as centimetres to metres //
## and centimetres                                 //
##                                                 //
##  centimetres     metres centimetres             //
##      110      ->    1       10                  //
##     1256      ->   12       56                  //
##///////////////////////////////////////////////////

a = int(input('what is the height:　'))

meters = a//100
centimeters = a%100

print(meters,':',centimeters)



