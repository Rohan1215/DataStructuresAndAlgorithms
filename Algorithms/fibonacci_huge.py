# Uses python3
import sys
def getPeriod(m):
    a=[0]
    f=0
    s=1
    p=0
    j=0
    while(True):
        p+=1
        a.append(s%m)
        temp=s
        s=s+f
        f=temp
        if(a[-2]==0 and a[-1]==1 and p>2):
            j=len(a)-2
            break
    return j,a[:-2]
def get_fibonacci_huge(n, m):
        period,arr=getPeriod(m)
        mod=n%period
        return arr[mod]
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
