# Uses python3
import sys
import random

def partition3(a, l, r):

    x = a[l]
    beforesame,aftersame=l+1,l
    for i in range(l+1,r+1):
        if(a[i]<=x):
            aftersame+=1
            a[i],a[aftersame]=a[aftersame],a[i]
            if(a[aftersame]<x):
                a[beforesame],a[aftersame]=a[aftersame],a[beforesame]  
                beforesame+=1
    a[l],a[beforesame-1]=a[beforesame-1],a[l]  
    return beforesame,aftersame
def randomized_quick_sort(a, l, r):
    if(l>=r):
        return 
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    p,p1 = partition3(a, l, r)
    randomized_quick_sort(a, l, p-1)
    randomized_quick_sort(a, p1+1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
