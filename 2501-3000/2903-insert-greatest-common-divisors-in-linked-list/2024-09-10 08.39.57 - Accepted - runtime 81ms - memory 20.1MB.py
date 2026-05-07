class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=self.LinkedToArr(head)
        return self.ArrToLinked([x for p in zip(t,[gcd(a,b) for a,b in pairwise(t)]) for x in p]+[t[-1]])


    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr=[]
        while head: 
            arr.append(head.val)
            head=head.next
        return arr