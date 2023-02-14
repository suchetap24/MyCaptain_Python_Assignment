def most_frequent():
    n=input('enter a string:')
    a={}
    for k in n:
        if k not in a:
            a[k]=1
        else:
            a[k]+=1
    b=sorted(a.items(),key=lambda x:x[1],reverse=True)
    for i,j in b:
        print(i,'=',j,'',end='')
most_frequent()        
        

