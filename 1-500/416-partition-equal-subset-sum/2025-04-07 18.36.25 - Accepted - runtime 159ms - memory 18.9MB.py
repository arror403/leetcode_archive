class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2!=0: return False
        
        target=s//2
        dp=set([0])
        
        for i in nums:
            # print(dp)
            next_dp=dp.copy()
            for t in dp:
                if t+i==target: return True

                next_dp.add(t+i)

            dp=next_dp


        return target in dp