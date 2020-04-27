# python3

from collections import namedtuple
Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])

class Buffer:    
    def __init__(self, size):
        self.size = size
        self.finish_time = []
    def is_full(self):
        if len(self.finish_time) == self.size:
            return True
        return False
    def is_empty(self):
        if len(self.finish_time) == 0:
            return True
        return False
    def last_element(self):
        return self.finish_time[-1]
    def flush_processed(self, request):
        while self.finish_time:
            if self.finish_time[0] <= request.arrival_time:
                self.finish_time.pop(0)
            else:
                break
    def process(self, request):
        self.flush_processed(request)
        if self.is_full==True:
            return Response(True, -1)
        if self.is_empty==True:
            self.finish_time = [request.arrived_at + request.time_to_process]
            return Response(False, request.arrived_at)

        response = Response(False, self.last_element)
        self.finish_time.append(self.finish_time[-1] + request.time_to_process)
        return response


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


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