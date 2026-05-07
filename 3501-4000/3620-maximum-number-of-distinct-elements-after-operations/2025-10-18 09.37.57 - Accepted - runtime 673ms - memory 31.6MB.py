class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        res = 0
        last = -inf

        nums.sort()

        for v in nums:
            mn = v - k
            mx = v + k
            if last < mn:
                last = mn
                res += 1
            elif last < mx:
                last += 1
                res += 1
        

        return res