class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)

        if ones: return n - ones

        res = inf
        for i in range(n):
            g = nums[i]
            for j in range(i + 1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    res = min(res, j - i)


        return -1 if res == inf else res + n - 1