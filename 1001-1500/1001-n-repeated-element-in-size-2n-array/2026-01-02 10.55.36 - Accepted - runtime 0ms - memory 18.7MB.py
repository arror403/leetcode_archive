class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        while 1:
            a, b = random.sample(nums, 2)
            if a == b: return a