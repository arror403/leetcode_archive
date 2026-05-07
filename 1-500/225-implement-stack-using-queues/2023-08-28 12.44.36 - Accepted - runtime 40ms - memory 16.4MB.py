class MyStack:

    def __init__(self):
        self.t=[]
        self.t = deque(self.t)

    def push(self, x: int) -> None:
        self.t.appendleft(x)

    def pop(self) -> int:
        tmp=self.t[0]
        self.t.popleft()
        return tmp

    def top(self) -> int:
        return self.t[0]

    def empty(self) -> bool:
        return len(self.t)==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()