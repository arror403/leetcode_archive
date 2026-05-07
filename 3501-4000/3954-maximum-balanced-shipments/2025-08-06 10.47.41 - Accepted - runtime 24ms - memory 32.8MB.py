class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        pre=res=0

        for w in weight:
            if w<pre:
                res+=1
                pre=0
            else:
                pre=w
 

        return res