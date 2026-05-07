class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def minPair(v):
            minSum = inf
            pos = -1

            for i in range(len(v) - 1):
                if (v[i] + v[i + 1]) < minSum:
                    minSum = v[i] + v[i + 1]
                    pos = i
            
            return pos

        res = 0
        
        while nums != sorted(nums):
            p = minPair(nums)
            nums[p] += nums[p + 1]
            del nums[p + 1]
            res += 1
        

        return res