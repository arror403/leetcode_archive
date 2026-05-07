class Solution:
    #ref: https://github.com/doocs/leetcode/blob/main/solution/2900-2999/2962.Count%20Subarrays%20Where%20Max%20Element%20Appears%20at%20Least%20K%20Times/README.md
    def countSubarrays(self, nums: List[int], k: int) -> int:
        M=max(nums)
        L=len(nums)
        res=cnt=j=0
        for x in nums:
            while j<L and cnt<k:
                cnt+=(nums[j]==M)
                j+=1
            if cnt<k: break
            res+=(L-j+1)
            cnt-=(x==M)
        return res