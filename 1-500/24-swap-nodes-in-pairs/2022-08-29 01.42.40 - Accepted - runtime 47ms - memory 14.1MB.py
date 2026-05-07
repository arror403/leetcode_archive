# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m=self.convertArr(head)
        res=[]
        for i in range(1,len(m),2):
            res.append(m[i])
            res.append(m[i-1])
            
        if len(m)%2==1: res.append(m[-1])
            
        return self.list2linked(res)
        
        
        
        
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