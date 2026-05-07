class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(i for i in nums if i>0)
        if not s: return 1

        for i in range(1,max(s)+1):
            if i not in s:
                return i

        return max(s)+1