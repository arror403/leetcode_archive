# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        list1=self.LinkedToArr(list1)
        list2=self.LinkedToArr(list2)
        
        res=[]
        
        for i in range(a): res.append(list1[i])
        
        for i in list2: res.append(i)
        
        for i in range(b+1,len(list1)): res.append(list1[i])        
        
        return self.ArrToLinked(res)
        
        
    def ArrToLinked(self, l):
        cur = dummy = ListNode(0)
        for n in l:
            cur.next = ListNode(n)
            cur = cur.next
        return dummy.next
        
        
    def LinkedToArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        return arr