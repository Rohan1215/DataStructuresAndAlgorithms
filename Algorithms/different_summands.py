# Uses python3
import sys

def optimal_summands(n):
    s = []
    q=1
    while(n>0):
        n-=q
        s.append(q)
        q+=1
    if(n<0):
        o=s.pop(-1)
        t=s.pop(-1)
        s.append(o+t+n)    
    return s

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
