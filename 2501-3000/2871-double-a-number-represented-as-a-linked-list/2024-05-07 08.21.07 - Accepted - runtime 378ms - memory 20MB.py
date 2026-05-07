# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sys.set_int_max_str_digits(10001)
        t=''

        while head:
            t+=str(head.val)
            head=head.next

        t=list(map(int,str(int(t)*2)))

        return self.ArrToLinked(t)


    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next