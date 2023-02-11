n=int(input('enter the no of terms:'))
n1=0
n2=1
count=0
if n==1:
    print(n1)
else:
    while count<n:
        print(n1)
        a=n1+n2
        n1=n2
        n2=a
        count+=1
   
    
    

