arr=[-10,-5,-2,4,7,9,15]
sum0=0
positivearr=[]
negativearr=[]
minarr=[]
arr.sort()
mini=0
for i in arr:
 if i<0:
  negativearr.append(i)
 if i>=0:
  positivearr.append(i)
print(positivearr)
print(negativearr)

if(sum0>=0):
 arr1=positivearr[:]
 while(len(arr1)!=0):
  var1=arr1.pop()
  diff=sum0-var1
  print("First instance of diff ",diff)
  if(diff>=0):
   print("This is diff ",diff)
   arr2=arr1[:]
   while(len(arr2)!=0):
    var2=arr2.pop(0)
    diff1=diff-var2
    if(diff1>=0):
     for i in positivearr:
      var3=i
      if(i-diff1==0):
       minarr=[var1,var2,var3]
       break
      else:
       mini=abs(sum(minarr)-sum0)
    else:
     for i in negativearr:
      var3=i
      if(i-diff1==0):
       minarr=[var1,var2,var3]
      else:
       mini=abs(sum(minarr)-sum0)  
        
  else:
   arr2=negativearr[:]
   while(len(arr1)!=0):
    var1=arr1.pop()
    diff=sum0-var1
   if(diff>=0):
    arr2=arr1[:]
    while(len(arr2)!=0):
     var2=arr2.pop(0)
     diff1=diff-var2
     if(diff1>=0):
      for i in positivearr:
       var3=i
       if(i-diff1==0):
        minarr=[var1,var2,var3]
        print(minarr)
        break
       else:
        mini=abs(sum(minarr)-sum0)
     else:
      for i in negativearr:
       var3=i
       if(i-diff1==0):
        minarr=[var1,var2,var3]
       else:
        mini=abs(sum(miniarr)-sum0)

#the sum is negtive       
else:
 arr1=negativearr[:]
 while(len(arr1)!=0):
  var1=arr1.pop()
  diff=sum0-var1
  print("First instance of diff ",diff)
  if(diff>=0):
   print("This is diff ",diff)
   arr2=arr1[:]
   while(len(arr2)!=0):
    var2=arr2.pop(0)
    diff1=diff-var2
    if(diff1>=0):
     for i in positivearr:
      var3=i
      if(i-diff1==0):
       minarr=[var1,var2,var3]
       break
      else:
       mini=abs(sum(minarr)-sum0)
    else:
     for i in negativearr:
      var3=i
      if(i-diff1==0):
       minarr=[var1,var2,var3]
      else:
       mini=abs(sum(minarr)-sum0)
 



print(minarr)
print(sum(minarr)) 
