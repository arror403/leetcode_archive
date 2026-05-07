# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.m=self.LinkedToArr(head)

    def getRandom(self) -> int:
        i=random.randint(0,len(self.m)-1)
        return (self.m[i])
    

    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()