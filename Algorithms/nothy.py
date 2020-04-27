#Uses python3
import sys
import math
import random

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str([self.x, self.y])

def distance(p1, p2):
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) **0.5

def construct_points(x, y):
    points = []
    for i in range(len(x)):
        points.append(Point(x[i], y[i]))
    return points

def mindist(x, y):
    points = construct_points(x, y)
    sorted_p_x = sorted(points, key=lambda p: p.x)

    return hugerecursion(sorted_p_x)

def threepoints(points):
    result = 99999999999
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            result = min(result, distance(points[i], points[j]))
    return result

def hugerecursion(p_x):
    size = len(p_x)

    if size <= 3:
        return threepoints(p_x)
    half_size = int(len(p_x)/2)
    lpx = p_x[0:half_size]
    rpx = p_x[half_size:size]
    lmin = hugerecursion(lpx)
    rmin = hugerecursion(rpx)
    mmin = min(lmin, rmin)

    li = (lpx[-1].x + rpx[0].x)/2
    hmin = compute_hybrid_min(lpx, rpx, li, mmin)

    return min(mmin, hmin)

def compute_hybrid_min(lx, rx, li, s):
    l = []
    for i in range(len(lx)):
        if abs(lx[i].x - li) <= s:
            l.append(lx[i])
    r = []
    for i in range(len(rx)):
        if abs(rx[i].x - li) <= s:
            r.append(rx[i])
    t = l + r
    
    t = sorted(t, key=lambda p: p.y)

    hybrid = s
    for i in range(len(t)):
        for j in range(i + 1, min(i+8, len(t))):
            if abs(t[i].y - t[j].y) <= s:
                hybrid = min(hybrid, distance(t[i], t[j]))

    return hybrid

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(mindist(x, y)))