# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=self.LinkedToArr(head)
        zero_i=[i for i,v in enumerate(arr) if v==0]
        L=len(zero_i)-1
        
        return self.ArrToLinked([sum(arr[zero_i[i]:zero_i[i+1]]) for i in range(L)])
        
        
    def ArrToLinked(self, arr):
        cur = dummy = ListNode(0)
        for n in arr:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr