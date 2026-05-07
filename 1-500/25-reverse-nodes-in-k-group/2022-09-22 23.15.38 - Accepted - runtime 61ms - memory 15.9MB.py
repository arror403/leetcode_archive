# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        m=self.LinkedToArr(head)
        res=[]
        l=0
        r,s=divmod(len(m),k)
        while r>0:
            tmp=m[l:l+k]
            tmp.reverse()
            res+=tmp
            l+=k
            r-=1
        res+=m[len(m)-s:]
        
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