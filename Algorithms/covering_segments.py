# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda a: a.end)
    boolarr=[False]*len(segments)
    for i in range(len(boolarr)):
        if(boolarr[i]):
            continue
        else:
            boolarr[i]=True
            points.append(segments[i].end)
            for j in range(i+1,len(boolarr)):
                if(segments[j].start<=segments[i].end<=segments[j].end):
                    boolarr[j]=True
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
