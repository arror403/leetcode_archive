# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        #step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt    
        slow.next = None
        
        #step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
#         res=[]
#         m=self.convertArr(head)
#         for i in range(len(m)//2):
#             res.append(m[i])
#             res.append(m[-(i+1)])
        
#         if len(m)%2==1: res.append(m[len(m)//2])
            
#         print(res)
        
#         head=self.list2linked(res)
#         # return self.list2linked(res)
        
        
        
        
#     def list2linked(self, l):
#         cur = dummy = ListNode(0)
#         for e in l:
#             cur.next = ListNode(e)
#             cur = cur.next
#         return dummy.next
        
        
#     def convertArr(self, head):
#         arr = []
#         curr = head
#         while (curr != None): 
#             arr.append(curr.val)
#             curr = curr.next
        
#         return arr