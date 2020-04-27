# Uses python3
def edit_distance(s, t):
    a=[[0 for i in range(len(s)+1)] for j in range(len(t)+1)]
    for i in range(len(s)+1):
        a[0][i]=i
    for j in range(len(t)+1):
        a[j][0]=j
    arr,p,g=edit(s,t,a)
    return rev(arr,p,g,s,t,0)
def edit(s,t,a):
    for j in range(1,len(s)+1):
        for i in range(1,len(t)+1):
            w=a[i][j-1]+1
            x=a[i-1][j]+1
            y=a[i-1][j-1]+1
            z=a[i-1][j-1]
            if(s[j-1]==t[i-1]):
                a[i][j]=min(w,x,z)
            else:
                a[i][j]=min(w,x,y)
    return a,i,j
def rev(a,i,j,s,t,n):
    if(i<=0 and j<=0):
        return n
    elif(j>0 and a[i][j]==a[i][j-1]+1):
        n+=1 

        n=rev(a,i,j-1,s,t,n)
    elif(i>0 and a[i][j]==a[i-1][j]+1):
        n+=1

        n=rev(a,i-1,j,s,t,n)
    else:
        if(s[j-1]!=t[i-1]):
            n+=1
 
        n=rev(a,i-1,j-1,s,t,n)

    return n


if __name__ == "__main__":
    print(edit_distance(input(), input()))