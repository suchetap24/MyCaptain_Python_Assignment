a=input('enter a file name:')
b=a.split('.')
c={'py':'python','java':'java','txt':'text'}
for i in c:
    if i==b[-1]:
        print('the extension of file name is',c[i])



