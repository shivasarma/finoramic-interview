#TODO: have to find out the redundant open brackets

#experimenting the given expression, has to be modified a lot
a='(a)'

#initilizing a counter
j=0

#initializing a boolean
checknext=False

#variable that holds the value of openbracket
openbracket=0
ob=0	#memory of redundant openbrackets
cb=0
redundancy=False
#variable that holds the degree of openbracket
degree=0

#loop that detects the brackets
for i in a:
 if i=='(':	#detecting open bracket
  if checknext==True: 	#boolean variable if checknext is true
   j=j+1
   checknext=True
   ob=j+1
  else:
   checknext=True
   ob=0
  if (j+1)>openbracket:
   openbracket=j+1	#variable that counts the maximum number of openbrackets
  
 elif i==')':		#condition if closed bracket is present
  if checknext==True:
   checknext=True 
   if ob>0:
    ob=ob-1
    cb=cb+1
    redundancy=True
  else:
   checknext=True

 else:
  j=0
  checknext=False

if redundancy==True:
 print(1)
else:
 print(0)

  

  
  


