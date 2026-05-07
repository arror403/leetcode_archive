class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.cap = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m={}


    def get(self, key: int) -> int:
        if key in self.m:
            resNode = self.m[key]
            ans = resNode.val

            self.m.pop(key)
            self.deleteNode(resNode)
            self.addNode(resNode)

            self.m[key] = self.head.next
            return ans
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            curr = self.m[key]
            self.m.pop(key)
            self.deleteNode(curr)

        if len(self.m) == self.cap:
            self.m.pop(self.tail.prev.key)
            self.deleteNode(self.tail.prev)

        self.addNode(Node(key, value))
        self.m[key] = self.head.next


    def addNode(self, newnode):
        temp = self.head.next

        newnode.next = temp
        newnode.prev = self.head

        self.head.next = newnode
        temp.prev = newnode
        
    def deleteNode(self, delnode):
        prevv = delnode.prev
        nextt = delnode.next

        prevv.next = nextt
        nextt.prev = prevv



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)