<<<<<<< HEAD
#TODO: find the sum of integers converged to a point
#Algorithm
#Sort the array
#pop the max value subtract it from sum
#create a sub array containing the values less than the sum
#iterate till convergence point is attained
#works only on positive integers```

arr=[1,3,5,8,18,40,94,10,48]
tot=61
miniarr=[arr[0],arr[1],arr[2]]
#sorting the array
arr1=arr	
arr1.sort()
convergence=0
var=[]
result=[]
#loop for removal of the numbers higher than the given sum
while(max(arr1)>tot):
 arr1.pop()
print("this is modified array")
print(arr1)
#for i in arr1:
# print(i)
while(len(arr1)!=0):
 var1=arr1.pop()
 diff=tot-var1
 if(diff>=var1):
  break
 arr2=arr1[:]
 arr3=[]
 print(arr2[0])
# while arr2[0]<diff :
#  arr3.append(arr2.pop(0))
 for i in arr2:
  if i<diff:
   arr3.append(i)
  else:
   break
 print("This is arr2",arr2)
 print("This is arr3",arr3)
 if(len(arr3)<3):
  consum=var1+arr1[0]+arr1[1]
  miniarr=[var1,arr1[0],arr1[1]]
  mini=abs(sum(miniarr)-tot)
 else:
  while(len(arr3)!=0):
   var2=arr3.pop()
   diff2=diff-var2
   if(diff2<=0):
    break
   for i in arr3:
    if diff2-i<0:
     break
    else:
     var3=i
   result=[var1,var2,var3]
   if(sum(result)-tot==0):
    mini=0
   elif(mini>abs(sum(result)-tot)):
    mini=abs(sum(result)-tot)
    miniarr=result
   else:
    continue
   print(mini)

 if(mini==0):
  break
print(sum(miniarr))
=======
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


>>>>>>> 6949037cecb7d46ef0c5901f24253e68f6b5490a
