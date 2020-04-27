# Uses python3
import sys
s=[]
def optimal_sequence(n):    
    arr=[]
    if(len(s[n])>1):
        return s[n]
    if(n/3==1):
        return [int(n),1]
    elif(n%3==0):
        i=int(n/3)
        s3=optimal_sequence(i)
        arr.append(s3)

    if(n/2==1):
        return [int(n),1]
    elif(n%2==0):
        w=int(n/2)
        s2=optimal_sequence(w)
        arr.append(s2)

    if(n-1==1):
        return [n,1]        
    elif(n-1>1):
        s1=optimal_sequence(n-1)
        arr.append(s1)
    arr.sort(key=lambda a: len(a))
    s[n].extend(arr[0])
    return s[n]
input = sys.stdin.read()
n = int(input)
for i in range(n+1):
    s.append([i])
if(n==2 or n==3):
    s[n]=[n,1]
if(n==0 or n==1):
    sequence=[n]
else:
    sequence=optimal_sequence(n)
print(len(sequence) - 1)
for x in sequence[::-1]:
    print(x, end=' ')
