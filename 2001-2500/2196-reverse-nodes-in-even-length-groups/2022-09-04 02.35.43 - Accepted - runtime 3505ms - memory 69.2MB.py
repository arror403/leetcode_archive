# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, m: Optional[ListNode]) -> Optional[ListNode]:
        m=self.LinkedToArr(m)
        x,res=0,[]
        while 1:
            x+=1
            i,j=self.Sum(x-1),self.Sum(x)
            if j>len(m):
                if (len(m)-i)%2==0:
                    tmp=m[i:]
                    tmp.reverse()
                    res+=tmp
                    break
                else:
                    res+=m[i:]
                    break
            elif x%2==0:
                tmp=m[i:j]
                tmp.reverse()
                res+=tmp
            else:
                res+=m[i:j]
    
        return self.ArrToLinked(res)
    
    
        
    def Sum(self, x):
        return int(x*(x+1)/2)
        
        
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