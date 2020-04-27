# Uses python3
import sys


def compute_min_refills(d, t, s):
    c=0
    if(t<s[0]):
        return -1
    s.append(d)
    ss=len(s)
    for i in range(ss):
        if(s[i]<s[-1] and s[i]+t<s[i+1]):
            return -1
        if(s[i]<s[-1] and s[i+1]>t):
            c+=1
            g=s[i]
            for p in range(ss):
                s[p]-=g
    return c


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
