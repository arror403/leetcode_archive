class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        present=[False]*100001
        for x in nums: present[x]=True
        
        dummy=ListNode(0, head)
        prev=dummy
        
        while prev.next:
            if present[prev.next.val]:
                prev.next=prev.next.next
            else:
                prev=prev.next
        

        return dummy.next