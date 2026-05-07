class Solution:
    def maxLength(self, nums: List[int]) -> int:
        m=[nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]

        return max([len(x) for x in m if reduce(lcm,x)*reduce(gcd,x)==reduce(operator.mul,x)])