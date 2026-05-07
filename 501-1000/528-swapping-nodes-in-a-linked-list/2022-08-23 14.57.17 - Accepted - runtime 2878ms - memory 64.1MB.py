# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        m=self.convertArr(head)
        m[-k],m[k-1]=m[k-1],m[-k]
        
        
        return self.list2linked(m)
        
        
        
    def list2linked(self, l):
        cur = dummy = ListNode(0)
        for e in l:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        
        
    def convertArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        
        return arr