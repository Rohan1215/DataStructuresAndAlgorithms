# Uses python3
import sys
def makeCool(a,b):
    temp=a%b
    a=b
    b=temp
    return a,b
def gcd_naive(a, b):
    a,b=max(a,b),min(a,b)
    while(b!=0):
        a,b=makeCool(a,b)
    return a

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
