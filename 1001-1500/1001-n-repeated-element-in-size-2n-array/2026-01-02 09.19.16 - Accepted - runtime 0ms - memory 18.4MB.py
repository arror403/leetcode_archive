class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        s=set()

        for v in nums:
            if v in s: return v
            else: s.add(v)


        return -1