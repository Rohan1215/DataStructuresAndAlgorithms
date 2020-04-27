#Uses python3

import sys
res=""
def funkyfunc(a,b):
    x=str(a)+str(b)
    y=str(b)+str(a)
    return a if x>=y else b

def largest_number(a):
    res=""
    while(a):
        maks=0
        for i in a:
            maks=funkyfunc(int(i),maks)
        res+=str(maks)

        a.remove(str(maks))

    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
