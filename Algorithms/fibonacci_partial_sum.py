# Uses python3
import sys

def fibonacci_partial_sum_naive(f, t):
    arr=[0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6, 3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7, 6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8, 4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]
    f1=(f%60)-1
    t1=t%60
    if(arr[t1]>=arr[f1]):
        return arr[t1]-arr[f1]
    else:
        return (arr[t1]+10)-arr[f1]


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))