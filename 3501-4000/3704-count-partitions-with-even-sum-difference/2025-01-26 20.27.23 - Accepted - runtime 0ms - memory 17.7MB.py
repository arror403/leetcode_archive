class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        S, m = sum(nums), list(accumulate(nums))
        m.pop()

        return sum((S-2*x)%2==0 for x in m)