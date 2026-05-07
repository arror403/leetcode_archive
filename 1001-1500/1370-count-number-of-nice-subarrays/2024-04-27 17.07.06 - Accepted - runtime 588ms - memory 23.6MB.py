class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        L=len(nums)
        dp=[1]+[0]*L
        res=0
        current_sum=0

        nums=list(map(lambda x:x%2,nums))

        for i in range(L):

            current_sum+=nums[i]

            if current_sum>=k:
                res+=dp[current_sum-k]

            if current_sum<=L:
                dp[current_sum]+=1


        return res