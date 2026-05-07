# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
#         cur = head
#         for N in range(1001):
#             if not cur: break
#             cur = cur.next
#         width, remainder = divmod(N, k)

#         ans = []
#         cur = head
#         for i in range(k):
#             h = cur
#             for j in range(width + (i < remainder) - 1):
#                 if cur: cur = cur.next
#             if cur:
#                 cur.next, cur = None, cur.next
#             ans.append(h)
#         return ans
        m=self.LinkedToArr(head)
        res=list(self.split(m,k))
        print(res)
        for i in range(len(res)): res[i]=self.ArrToLinked(res[i])
            
        return res
        
        
    def split(self, a, n):
        k, m = divmod(len(a), n)
        return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))        
        
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