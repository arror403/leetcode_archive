# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Create a temporary node
        temp = ""
        while (head != None):
    
            # This condition is for the case
            # when there is no loop
            if (head.next == None):
                return False
    
            # Check if next is already
            # pointing to temp
            if (head.next == temp):
                return True
    
            # Store the pointer to the next node
            # in order to get to it in the next step
            next = head.next
    
            # Make next point to temp
            head.next = temp
    
            # Get to the next node in the list
            head = next
    
        return False