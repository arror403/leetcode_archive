# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m=self.LinkedToArr(head)
        i,j=0,0
        r,res=[],[]
        for i in range(len(m)): 
            if m[i]==0:
                r.append(i)
        
        for i in range(len(r)-1): res.append(sum(m[r[i]:r[i+1]]))
            
        return self.ArrToLinked(res)
        
        
        
    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr