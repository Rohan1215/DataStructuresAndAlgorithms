# python3
from collections import deque

def max_sliding(s, k):
    kyu=deque()
    for i in range(k):
        while kyu:
            if(s[i]>s[kyu[-1]]):
                kyu.pop()
            else:
                break
        kyu.append(i)

    for i in range(k,len(s)):
        print(str(s[kyu[0]]),end=" ")
        while kyu and kyu[0]<=i-k:
            kyu.popleft()
        while kyu:
            if(s[i]>s[kyu[-1]]):
                kyu.pop()
            else:
                break
        kyu.append(i)
    print(s[kyu[0]]) 
        

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    max_sliding(input_sequence, window_size)