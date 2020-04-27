#Uses python3
import sys
import math
def calc(x1,y1,x2,y2):
    return math.sqrt(((x1-x2)**2)+((y1-y2)**2))
def mindist(x, y):
    if(len(x)==2):
        return calc(x[0],y[0],x[1],y[1])
    if(len(x)<2):
        return 3000
    mid=len(x)//2
    min1=mindist(x[:mid],y[:mid])
    min2=mindist(x[mid:],y[mid:])
    d=min([min1,min2])
    c=[]
    p=[]
    for a in x:
        if x[mid]-d<=a<=x[mid]:
            c.append([x[a],y[a]])
        if x[mid]<=a<=x[mid]+d:
            p.append([x[a],y[a]])
    c.sort(key=lambda a:a[1])
    finalmin=name(c,p,d)
    return finalmin
def name(c,p,d):
    m=d
    for i in c:
        for j in p:
            if i[0]+d>=j[0]>=i[0] and i[1]-d<=j<=i[1]+d:
                t=calc(i[0],i[1],j[0],j[1]) 
                m=m if m<=t else t
    return m
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(mindist(x, y)))
