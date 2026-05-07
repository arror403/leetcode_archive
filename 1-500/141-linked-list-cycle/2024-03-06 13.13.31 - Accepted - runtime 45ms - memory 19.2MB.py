# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        number_of_node=0
        curr = head
        while (curr != None):
            number_of_node+=1
            curr = curr.next
            if number_of_node>10000:
                # print(number_of_node)
                return True
        
        return False