# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        t=head.next
        s=0
        cur=res=ListNode()

        while t:
            if t.val!=0:
                s+=t.val
                t=t.next
            else:
                cur.next=ListNode(s)
                s=0
                cur=cur.next
                t=t.next

                
        return res.next