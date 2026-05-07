class Solution:
    def maxSum(self, nums: List[int]) -> int:
        m=[nums[i:j] for i in range(len(nums)) for j in range(i+1, len(nums)+1)]
        res=[]

        for s in m:
            if max(s)<0:
                res.append(max(s))
            else:
                res.append(sum(set(x for x in s if x>=0)))

        
        return max(res)