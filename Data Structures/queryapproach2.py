# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process","lab"])

class Node:
    def __init__(self,arrivalTime,dur,label):
        self.next=None
        self.arrivalTime=arrivalTime
        self.dur=dur
        self.constantdur=dur
        self.label=label
    def isEmpty(self):
        return self.dur==0


class LinkedList:
    def __init__(self, size):
        self.max = size
        self.listsize=0
        self.head=None
        self.tail=None
    def Push(self,arv,dur,label):
        node=Node(arv,dur,label)
        if not(self.head):
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.listsize+=1
    def POP(self):
        if(self.head==self.tail):
            self.tail=None
            self.head=None
        else:
            self.head=self.head.next
        self.listsize-=1
    def PopAfter(self,x):
        x.next=x.next.next
        self.listsize-=1
    def process(self):
        thing=[]
        if self.head:
            while self.head.constantdur==0:
                thing.append(self.head)
                self.POP()
                if not self.head:
                    break
        if(self.head):
            self.head.dur-=1
            if self.head.isEmpty():
                a=self.head
                self.POP()
                return a,thing
            else:
                return None,thing
        else:
            return None,thing

        
            

def process_requests(arr, LL):
    fin=[None]*len(arr)
    time=0

    while fin.count(None)>0:
        nud,ting=LL.process()
        if nud:
            fin[nud.label]=time-nud.constantdur
        if ting:
            for i in ting:
                fin[i.label]=time-1
        if arr:    
            while(arr[0].arrived_at<time):
                fin[arr[0].lab]=-1
                arr.pop(0)
                if not arr:
                    break
        sub=LL.max-LL.listsize
        if(len(arr)-1>=sub):
            t=arr[sub-1].arrived_at
            while (arr[sub-1].time_to_process==0):
                if(arr[sub].arrived_at==t):
                    sub+=1
                    if(sub)>=len(arr)-1:
                        break
                else:
                    break
        for _ in range(sub):
            if arr:
                if arr[0].arrived_at==time:
                    o=arr[0].arrived_at
                    p=arr[0].time_to_process
                    q=arr[0].lab
                    arr.pop(0)
                    LL.Push(o,p,q)
        time+=1
        
        



    return fin

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at,time_to_process,i))

    LL = LinkedList(buffer_size)
    ans = process_requests(requests, LL)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
