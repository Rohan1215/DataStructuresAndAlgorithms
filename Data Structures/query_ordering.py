# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
    def isEmpty(self):
        return len(self.finish_time)==0
    def isFull(self):
        if(len(self.finish_time))==(self.size):
            return True
        return False 
    def deyeet(self,req):
        while self.finish_time:
            if(self.finish_time[0]<=req.arrived_at):
                self.finish_time.pop(0)
            else:
                break

    def process(self, request):
        self.deyeet(request)
        if len(self.finish_time)==self.size:           
            return Response(True,-1)
        if len(self.finish_time)==0:
            self.finish_time=[request.arrived_at+request.time_to_process]
            return Response(False,request.arrived_at)
        r=Response(False,self.finish_time[-1])
        self.finish_time.append(self.finish_time[-1] + request.time_to_process)
        return r


def process_requests(requests, buffer):
    return [buffer.process(r) for r in requests]


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
