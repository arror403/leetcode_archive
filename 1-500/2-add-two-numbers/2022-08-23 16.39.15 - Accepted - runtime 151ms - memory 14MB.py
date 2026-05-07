# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m=self.convertArr(l1)
        n=self.convertArr(l2)
        
        m=[str(x) for x in m]
        m.reverse()
        m=int(''.join(m))
        
        n=[str(x) for x in n]
        n.reverse()
        n=int(''.join(n))

        res=m+n
        
        res=list(map(int,str(res)))
        
        res.reverse()
        
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