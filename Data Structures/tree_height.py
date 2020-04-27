# python3

import sys
import threading
class Node:
    def __init__(self,key):
        self.key=key
        self.childArr=[]
    def getKey(self):
        return self.key
    def addKid(self,K):
        self.childArr.append(K)
def makeTree(n,parents):
    arr=[None]*n
    root=0
    for i in range(n):
        arr[i]=Node(i)
    for index in range(n):
        val=parents[index]
        if(val==-1):
            root=index
        else:
            arr[val].addKid(arr[index])
    return arr,root
def compute_height(tre):
    if not tre:
        return 0
    else:
        K=tre.childArr
        m=0
        for i in K:
            j=compute_height(i)
            m=max(j,m)
        return m+1

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    arr,root=makeTree(n,parents)
    num=compute_height(arr[root])
    print(num)


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
