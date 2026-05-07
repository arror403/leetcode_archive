# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d=[]

        while head:
            d.append(head.val)
            head=head.next

        return reduce(lambda ll,data: (ll := ListNode(data, ll)), d, None)