class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        
        pos=[i for i in range(1,len(arr)-1) if self.isCritical(arr[i-1],arr[i],arr[i+1])]

        return [-1,-1] if (len(pos)<=1) else [min([b-a for a,b in pairwise(pos)]), pos[-1]-pos[0]]


    def isCritical(self, b, cur, n):
        return ((b<cur and cur>n) or (b>cur and cur<n))