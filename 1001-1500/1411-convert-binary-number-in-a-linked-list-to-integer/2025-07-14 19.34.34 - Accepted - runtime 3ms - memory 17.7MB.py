class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return int(''.join(str(x) for x in self.LinkedToArr(head)), 2)
        
        
    def LinkedToArr(self, head):
        arr=[]
        while head: 
            arr.append(head.val)
            head=head.next
        return arr