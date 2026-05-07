class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        t=1
        y=0
        while 1:
            if t not in arr:
                y+=1
            if y==k:
                break
            t+=1
        return t