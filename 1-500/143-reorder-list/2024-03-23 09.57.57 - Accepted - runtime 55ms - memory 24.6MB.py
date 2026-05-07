# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    ##### power by chatGPT #####
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Split the list into two halves
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge the two halves alternatively
        first = head
        second = prev
        while second.next:
            temp = first.next
            first.next = second
            first = temp
            
            temp = second.next
            second.next = first
            second = temp