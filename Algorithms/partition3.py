# Uses python3
import sys
import itertools

def partition3(A):
    s=sum(A)//3
    if(sum(A)%3>0):
        return 0
    arr=[[0 for i in range(s+1)] for j in range(len(A)+1)]
    return arr
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

