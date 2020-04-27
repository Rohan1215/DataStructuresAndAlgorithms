# Uses python3
import sys

def optimal_weight(m, w):
    arr=[[0 for i in range(m+1)] for j in range(len(w)+1)]

    for i in range(1,len(w)+1):
        for j in range(1,m+1):
            arr[i][j]+=arr[i-1][j]
            if(w[i-1]<=j):
                n=arr[i-1][j-w[i-1]]+w[i-1]
                if n> arr[i][j]:
                    arr[i][j]=n
    return(arr[-1][-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
