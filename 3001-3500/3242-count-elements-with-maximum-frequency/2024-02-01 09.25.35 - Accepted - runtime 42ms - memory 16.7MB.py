class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums).values()
        m=max(c)
        return sum(i for i in c if i==m)