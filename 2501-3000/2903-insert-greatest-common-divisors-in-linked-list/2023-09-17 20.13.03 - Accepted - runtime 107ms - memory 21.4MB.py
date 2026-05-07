# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=self.LinkedToArr(head)
        c=[]
        res=[]
        for i in range(len(t)-1):
            c.append(math.gcd(t[i],t[i+1]))
        for i in range(len(c)):
            res.append(t[i])
            res.append(c[i])

        res.append(t[-1])

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