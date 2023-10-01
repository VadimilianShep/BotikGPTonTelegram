
a = int(input())
b = int(input())

def F(a,b):
    while(b>0):       
        b=b-1
        a=a+1
        F(a,b)
    return a
   
a = F(a,b)

print (a)
 