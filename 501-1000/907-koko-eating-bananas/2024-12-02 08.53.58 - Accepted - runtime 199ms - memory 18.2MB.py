class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def feasible(speed):
            return sum((p-1)//speed+1 for p in piles)<=h

        l,r=1,max(piles)

        while l<r:
            mid=l+(r-l)//2

            if feasible(mid): r=mid
            else: l=mid+1


        return l