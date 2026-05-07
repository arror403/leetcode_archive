class Solution:
    
    ##### power by Claude #####

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:  # Empty list or single node is a palindrome
            return True

        # Step 1: Find the middle node using the slow and fast pointers
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow.next
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Compare the first half with the reversed second half
        p1, p2 = head, prev
        is_palindrome = True
        while p2:
            if p1.val != p2.val:
                is_palindrome = False
                break
            p1 = p1.next
            p2 = p2.next

        # Step 4: Restore the original linked list by reversing the second half again
        prev = None
        curr = prev
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return is_palindrome