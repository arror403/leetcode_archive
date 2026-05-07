# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nums=self.LinkedToArr(head)

        max_right = nums[-1]  # Start with the last element
        result = [max_right]

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= max_right:
                result.append(nums[i])
                max_right = nums[i]

        return self.ArrToLinked(reversed(result))


    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        res=[]
        while head: 
            res.append(head.val)
            head=head.next
        return res