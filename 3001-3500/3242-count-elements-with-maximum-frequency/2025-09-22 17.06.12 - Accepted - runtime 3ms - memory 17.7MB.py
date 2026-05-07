class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=Counter(nums).values()
        m=max(d)

        return sum(i for i in d if i==m)