class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        r = [nums[i:j] for i in range(len(nums)) for j in range(i + 1, len(nums) + 1)]
        res=-inf
        for i in r:
            if self.isAscending(i):
                if sum(i)>res:
                    res=sum(i)

        return res

    def isAscending(self, m):
        for i in range(len(m)-1):
            if m[i]<m[i+1]: continue
            else: return False
        return True