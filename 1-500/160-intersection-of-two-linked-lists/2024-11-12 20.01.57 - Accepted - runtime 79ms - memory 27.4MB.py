class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if (headA==None or headB==None): return None
        
        a,b=headA,headB
        
        while a!=b:
            a=headB if a==None else a.next
            b=headA if b==None else b.next


        return a