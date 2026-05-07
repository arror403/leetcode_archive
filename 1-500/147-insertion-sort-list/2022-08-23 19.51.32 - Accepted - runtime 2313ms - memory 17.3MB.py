# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.list2linked(self.insertionSort(self.convertArr(head)))
        
        
        
        
    def list2linked(self, l):
        cur = dummy = ListNode(0)
        for e in l:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy.next
        
        
    def convertArr(self, head):
        arr = []
        curr = head
        while (curr != None): 
            arr.append(curr.val)
            curr = curr.next
        
        return arr
        
        
    def insertionSort(self, array):
        for step in range(1, len(array)):
            key = array[step]
            j = step - 1

            # Compare key with each element on the left of it until an element smaller than it is found
            # For descending order, change key<array[j] to key>array[j].        
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j = j - 1

            # Place key at after the element just smaller than it.
            array[j + 1] = key
        return array