class Node:
    def __init__(self, val=0, m=inf, next=None):
        self.val = val
        self.m = m
        self.next = next

class MinStack:

    def __init__(self):
        self.head=Node()

    def push(self, val: int) -> None:
        if self.head is None: 
            self.head = Node(val, val, None)
        else:
            self.head = Node(val, min(val, self.head.m), self.head)

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.m