class MyCircularDeque:

    def __init__(self, k: int):
        self.d=deque()
        self.max_len=k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return 0
        else:
            self.d.appendleft(value)
        return 1

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return 0
        else:
            self.d.append(value)
        return 1

    def deleteFront(self) -> bool:
        if self.d:
            self.d.popleft()
            return 1
        else:
            return 0

    def deleteLast(self) -> bool:
        if self.d:
            self.d.pop()
            return 1
        else:
            return 0

    def getFront(self) -> int:
        if self.d:
            return self.d[0]
        else:
            return -1

    def getRear(self) -> int:
        if self.d:
            return self.d[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return len(self.d)==0

    def isFull(self) -> bool:
        return len(self.d)==self.max_len