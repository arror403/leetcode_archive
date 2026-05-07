class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res=0

        while (nums and nums[0]<k):
            x=heappop(nums)
            y=heappop(nums)
            heappush(nums, 2*x+y)
            res+=1


        return res