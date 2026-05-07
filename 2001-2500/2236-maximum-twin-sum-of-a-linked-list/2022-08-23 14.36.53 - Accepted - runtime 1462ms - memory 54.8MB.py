# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        m=self.convertArr(head)
        res=-inf
        
        for i in range(0,len(m)//2+1):
            if (m[i]+m[len(m)-i-1])>res:
                res=(m[i]+m[len(m)-i-1])
                
        return res

        
    def convertArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        
        return arr