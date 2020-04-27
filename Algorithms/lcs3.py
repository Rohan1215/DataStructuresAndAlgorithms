#Uses python3

import sys

def lcs3(a, b, c):
    arr=[[[0 for k in range(len(c)+1)]for j in range(len(b)+1)] for i in range(len(a)+1)]
    return coolfunction(a,b,c,arr)
def coolfunction(a,b,c,arr):
    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            for k in range(1,len(c)+1):
                if(a[i-1]==b[j-1] and a[i-1]==c[k-1]):
                    arr[i][j][k]=max(arr[i-1][j-1][k-1]+1, arr[i-1][j-1][k], arr[i-1][j][k-1], arr[i][j-1][k-1], arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])
                else:
                    arr[i][j][k]=max(arr[i-1][j-1][k-1], arr[i-1][j-1][k], arr[i-1][j][k-1], arr[i][j-1][k-1], arr[i-1][j][k], arr[i][j-1][k], arr[i][j][k-1])
    return arr[-1][-1][-1]                 


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
