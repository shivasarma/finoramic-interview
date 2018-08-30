from collections import deque

a='(a+(b+(c)))+((a+b))+(a+(b+(c)))'

lst=deque(a)
red=0

while len(lst)!=0:
 
 if lst.pop()==')':
  if lst.pop()==')':
   while len(lst)!=0:
    if lst.pop()=='(':
     if lst.pop()=='(':
      red=1
     else:
      break


print(red)


