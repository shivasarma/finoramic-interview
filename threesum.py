#TO DO: this is a program to determine the closest sum of three integers provided in an array.

#Algorithm: => Determine an array of n elements
#           =>arrange the elements in ascending order
#           =>Condition 1: if all the integers are either positive or negative. Converge all the numbers to the given sum and perform all the combinations
#           =>Condition 2: Provided with negative sum there is at least a single integer which is negative. Hence start all the iterations from negative
#


#imports

import numpy ,math

#initiating an array
#a=[11,22,-5,-87,54,3,-4,57,74,-7,58,96,-78,83]
a=[1,11,51,25,104,35,57,45,32,14,32]
#demo c
c=51

#sorting the array in ascending order
b=numpy.sort(a)

#summing up the array
sum=sum(a)

#determining an array as postive, negative.
arrtype="null"

for i in b:
    if i > 0:
        arrtype="positive"
    else:
        break
for i in b:
    if i < 0:
        arrtype="negative"
    else:
        break
d=numpy.empty(0,int)

#Algorithm for array of positive numbers
if(arrtype=="positive"):
    for i in b:
        if i < c:   #making a new array that all the elements provide sum of that element
            d = numpy.append(d,i)
        else:
            break
    #we got a new array containing only those elements with the numbers within the range of give positive number
    arr_asc=d
    arr_dsc=d[::-1]
    
print a
print b
print c
print d


