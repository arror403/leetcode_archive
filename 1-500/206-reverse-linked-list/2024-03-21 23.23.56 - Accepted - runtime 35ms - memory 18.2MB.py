# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=deque()

        while head:
            d.appendleft(head.val)
            head=head.next

        cur=dummy=ListNode(0)
        
        for n in d:
            cur.next=ListNode(n)
            cur=cur.next

        return dummy.next