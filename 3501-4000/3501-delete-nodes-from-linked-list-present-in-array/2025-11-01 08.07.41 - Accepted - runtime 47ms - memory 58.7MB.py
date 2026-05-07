# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        s=set(nums)
        while head.val in s: head=head.next
        pre=head
        res=head

        if head.next:
            head=head.next
            while head:
                if head.val not in s:
                    pre.next=head
                    pre=head
                head=head.next

            if pre.next and pre.next.val in s:
                pre.next=None


        return res