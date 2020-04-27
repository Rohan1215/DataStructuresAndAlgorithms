# Uses python3
import sys

def get_number_of_inversions(a):
    if len(a) == 1:
        return 0,a
    ave = (len(a))// 2
    f,b= get_number_of_inversions(a[:ave])
    g,c= get_number_of_inversions(a[ave:])
    inv,Q=Merge(b,c)
    return inv+g+f,Q
def Merge(b,c):
    inv=0
    A=[]
    while(b and c):
        if(b[0]<=c[0]):
            A.append(b.pop(0))
        else:
            inv+=len(b)
            A.append(c.pop(0))
    if(b):
        A+=b
    elif(c):
        A+=c
    return inv,A
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a)[0])
