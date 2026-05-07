# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=self.LinkedToArr(head)
        pos=[i for i in range(1,len(arr)-1) if self.isCritical(arr[i-1],arr[i],arr[i+1])]
        L=len(pos)

        if (L<=1): return [-1,-1]

        m=inf
        for i in range(1,L): m=min(m, pos[i]-pos[i-1])


        return [m, pos[-1]-pos[0]]


    def isCritical(self, b, cur, n):
        return ((b<cur and cur>n) or (b>cur and cur<n))        
        
        
    def LinkedToArr(self, head):
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        return arr