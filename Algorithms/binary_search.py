# Uses python3
import sys

def bs(a, x):
    l, r = 0, len(a)
    i=r//2
    while(x!=a[i]):
        if(x>a[i]):
            l=i
        elif(x<a[i]):
            r=i
        i=l+((r-l)//2)
        if(r-l==1):
            if(a[l]==x):
                return l
            return -1
    return i
    


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(bs(a, x), end = ' ')
