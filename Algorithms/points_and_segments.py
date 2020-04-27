# Uses python3
import sys

def fast_count_segments(points,starts,ends):
    for i in range(len(starts)):
        starts[i]=[starts[i],1]
    for i in range(len(ends)):
        ends[i]=[ends[i],3]
    for i in range(len(points)):
        points[i]=[points[i],2,i]
    arr=starts+points+ends
    arr.sort(key=lambda a:a[0])
    c=0
    final=[]
    for i in arr:
        if i[1]==1:
            c+=1
        elif i[1]==3:
            c-=1
        else:
            final.append([c,i[2]])
    final.sort(key=lambda a: a[1])
    return final

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    ranges=[] 
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(points,starts,ends)
    for x in cnt:
        print(x[0], end=' ')
