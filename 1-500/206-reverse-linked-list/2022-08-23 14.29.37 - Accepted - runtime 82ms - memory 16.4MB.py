# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.list2linked(self.convertArr(head)[::-1])
        
        
    def convertArr(self, head):
        arr = []
        curr = head
        # Traverse the Linked List and add the
        # elements to the array one by one
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr
    
    
    def list2linked(self, l):
        cur = dummy = ListNode(0)
        for e in l:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next