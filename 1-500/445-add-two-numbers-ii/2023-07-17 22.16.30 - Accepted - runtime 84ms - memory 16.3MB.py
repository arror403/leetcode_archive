# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        
        # Push the elements of l1 into stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # Push the elements of l2 into stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        carry = 0
        head = None
        
        while stack1 or stack2 or carry:
            # Perform the addition with carry
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0
            total = val1 + val2 + carry
            
            carry = total // 10
            total %= 10
            
            # Create a new node for the result
            new_node = ListNode(total)
            
            # Connect the new node to the previous result
            new_node.next = head
            head = new_node
        
        return head