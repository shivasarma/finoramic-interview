arr=[-10,-5,-2,4,7,9,15]
sum=0
positivearr=[]
negativearr=[]

arr.sort()
for i in arr:
 if i<0:
  negativearr.append(i)
 if i>=0:
  positivearr.append(i)
print(positivearr)
print(negativearr)
#if(sum>=0)

