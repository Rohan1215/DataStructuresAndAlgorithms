# Uses python3
def ev(a,op,b):
    a=int(a)
    b=int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
def MakeArray(op,num,maxarr,minarr):
    for a in range(len(maxarr)):
        maxarr[a][a],minarr[a][a]=int(num[a]),int(num[a])
    for a in range(1,len(minarr)):
        for i in range(len(minarr)-a):
            j=i+a
            maxarr[i][j],minarr[i][j]=MinMax(i,j,op,num,maxarr,minarr)
    return maxarr[0][len(maxarr)-1]
def MinMax(i,j,op,num,maxarr,minarr):
    b=-100000
    s=100000
           
    for a in range(i,j):
        x=ev(maxarr[i][a],op[a],maxarr[a+1][j])
        y=ev(maxarr[i][a],op[a],minarr[a+1][j])
        z=ev(minarr[i][a],op[a],maxarr[a+1][j])
        d=ev(minarr[i][a],op[a],minarr[a+1][j])
        b=max(b,x,y,z,d)
        s=min(s,x,y,z,d)
    return b,s
def get_maximum_value(s):
    op=[]
    num=[]
    for a in s:
        if a.isdigit():
            num.append(a)
        else:
            op.append(a)
    maxarr=[[0 for i in range(len(op)+1)] for j in range(len(op)+1)]
    smarr=[[0 for i in range(len(op)+1)] for j in range(len(op)+1)]
    ZEANSWER=MakeArray(op,num,maxarr,smarr)


    return ZEANSWER
if __name__ == "__main__":
    print(get_maximum_value(input()))
