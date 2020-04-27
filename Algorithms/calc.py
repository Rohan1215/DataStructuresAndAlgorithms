# Uses python3
import sys
s=[]
def func(n):

    ans=seq(n)
    return actual(ans,n)
def seq(n):
    for i in range(2,n+1):
        m1=s[i-1]
        m2=10000000
        m3=10000000
        if(i%3==0):
            m3=s[int(i/3)]
        if(i%2==0):
            m2=s[int(i/2)]
        m=min(m1,m2,m3)
        s[i]=m+1
    return s
def actual(a,n):
    p=[]
    while n>=1:
        p.append(n)
        if(n%2==0 and n%3==0):
            n=n//3
        elif(n%2!=0 and n%3!=0):
            n-=1
        elif(n%3==0):
            if(a[n-1]<a[n//3]):
                n-=1
            else:
                n=n//3
        elif(n%2==0):
            if(a[n-1]<a[n//2]):
                n-=1
            else:
                n=n//2
    return p
input = sys.stdin.read()
n = int(input)
s=[0]*(n+1)
sequence = list(func(n))
if(n==1):
    sequence=[1]
print(len(sequence) - 1)
for x in sequence[::-1]:
   print(x, end=' ')
