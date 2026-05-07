class Router:

    def __init__(self, memoryLimit: int):
        self.mpp=defaultdict(int)           # to track duplicates
        self.queue=deque()                  # to store packets in FIFO order
        self.timestamps=defaultdict(list)   # for timestamps tracking
        self.st=defaultdict(int)
        self.maxSize = memoryLimit

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        # checking for duplicate
        if packet in self.mpp: return False
        if len(self.queue) == self.maxSize: # remove the first element if queue is full
            res = self.queue[0]
            del self.mpp[res]
            temp = res[1]
            self.st[temp]+=1
            self.queue.popleft()
        self.queue.append(packet)

        # self.mpp[packet]+=1
        self.mpp[packet]=1
        
        self.timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue: return []
        res = self.queue.popleft()
        del self.mpp[res]
        temp = res[1]
        self.st[temp]+=1
        return res        

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.timestamps: return 0
        p = self.timestamps[destination]
        temp = self.st[destination]
        # for t in range(p[0]+temp, p[-1]):
        #     if t<startTime: 
        #         right=t
        #         break
        # f=1
        # for t in range(p[0]+temp, p[-1]):
        #     if t>endTime:
        #         f=0
        #         left=t
        #         break
        # if f: left=endTime
        right = bisect.bisect_left(p, startTime, temp)
        left = bisect.bisect_right(p, endTime, temp)
        return (left - right)