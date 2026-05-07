class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # if len(nums)<=5: return sum(nums)/len(nums)
        # res=-inf
        # for i in range(len(nums)-k+1):
            #   print(nums[i:i+k])
        #     tmp=sum(nums[i:i+k])/k
        #     if tmp>res: res=tmp

        # return res
        res = -inf
        window_sum = sum(nums[:k])
        res = max(res, window_sum / k)
        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i-k]
            res = max(res, window_sum / k)
        return res