# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m=self.LinkedToArr(head)
        x,res=0,[]
        # res.append(m[0])
        
        while 1:
            x+=1
            
            if self.Sum(x)>len(m):
                if (len(m)-self.Sum(x-1))%2==0:
                    tmp=m[self.Sum(x-1):]
                    tmp.reverse()
                    res+=tmp
                    break
                else:
                    res+=m[self.Sum(x-1):]
                    break
            
            elif x%2==0:
                tmp=m[self.Sum(x-1):self.Sum(x)]
                tmp.reverse()
                res+=tmp
                # print(x,self.Sum(x-1),self.Sum(x))
            else:
                res+=m[self.Sum(x-1):self.Sum(x)]
                # print(x,self.Sum(x-1),self.Sum(x))
    

            
            
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