# Uses python3
import sys

def getmaggie(arr, left, right):
    if(left+1==right):
        return [[arr[left]],[]]
    mid=left+(right-left)//2
    a=getmaggie(arr,left,mid)
    b=getmaggie(arr,mid,right)
    return funkywunky(a,b)
def funkywunky(a,b):
    x1,x2=coolfunc(a[0],b[1])
    y1,y2=coolfunc(b[0],a[1])
    
    if(x1[0]==y1[0]):
        return [x1+y1,x2+y2]
    elif(len(x1)>len(y1)):
        return [x1,y1+x2+y2]
    else:
        return [y1,x1+x2+y2]



def coolfunc(m,rest):
    r=[]
    for i in rest:
        if i==m[0]:
            m.append(i)
        else:
            r.append(i)
    return m,r

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    q=len(getmaggie(a,0,n)[0])
    if q > n//2:
        print(1)
    else:
        print(0)
