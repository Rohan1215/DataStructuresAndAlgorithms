#python3
import sys

class StackWithMax():
    def __init__(self):
        self.stack = []
        self.maxarr=[]
        self.max=0

    def Push(self, a):
        self.stack.append(a)
        num=max(a,self.max)
        self.maxarr.append(num)
        self.max=num
    def Pop(self):
        self.stack.pop(-1)
        self.maxarr.pop(-1)

    def Max(self):
        return self.maxarr[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
