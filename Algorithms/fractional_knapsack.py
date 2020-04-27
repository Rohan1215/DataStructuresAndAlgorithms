# Uses python3
import sys

def get_optimal_value(c, w, v):
    count=0
    arr=[]
    for i in range(len(w)):
        arr.append([v[i],w[i],v[i]/w[i]])
    arr.sort(reverse=True,key=lambda o: o[2])
    for i in range(len(w)):
        while(c>0 and arr[i][1]>0):
            c-=1
            arr[i][1]-=1
            count+=arr[i][2]
    return count    


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
