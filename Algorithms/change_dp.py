# Uses python3
import sys
a=[4,3,1]
q=[]
def get_change(m):
    if(q[m-1]!=0):
        return q[m-1]
    for i in range(1,m+1):
        q[i-1]=i-1
        for j in a:
            if(q[i-1]>=j):
                r=get_change(i-j)+1
                q[i-1]=min([r,q[i-1]])
    return q[m-1]
if __name__ == '__main__':
    m = int(sys.stdin.read())
    m+=1
    q=[0]*m
    print(get_change(m))

