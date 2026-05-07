class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res=self.split(self.LinkedToArr(head), k)

        for i in range(len(res)): res[i]=self.ArrToLinked(res[i])

        return res
        
        
    def split(self, a, n):
        k,m = divmod(len(a), n)
        return list(a[i*k + min(i,m) : (i+1)*k + min(i+1,m)] for i in range(n))  
        
        
    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr = []
        while head: 
            arr.append(head.val)
            head=head.next
        return arr