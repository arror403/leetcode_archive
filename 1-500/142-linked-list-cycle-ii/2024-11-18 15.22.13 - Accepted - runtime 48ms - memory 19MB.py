class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break

        if not (fast and fast.next): return None

        while head != slow:
            head = head.next
            slow = slow.next


        return head