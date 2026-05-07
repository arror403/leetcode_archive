class Solution:
    ##### power by Claude #####
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Initialize slow and fast pointers
        slow = head
        fast = head
        
        # Move the fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When the fast pointer reaches the end,
        # the slow pointer will be at the middle
        return slow