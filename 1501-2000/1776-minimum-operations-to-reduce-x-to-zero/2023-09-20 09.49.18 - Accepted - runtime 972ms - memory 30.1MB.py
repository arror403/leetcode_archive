class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target = total_sum - x
        
        if target < 0:
            return -1

        res = float('inf')
        current_sum = 0
        left = 0

        for right in range(len(nums)):
            current_sum += nums[right]
            
            while current_sum > target and left <= right:
                current_sum -= nums[left]
                left += 1
                
            if current_sum == target:
                res = min(res, len(nums) - (right - left + 1))

        return res if res != float('inf') else -1
        
        # res=0
        # nums=deque(nums)
        # while nums:
        #     if nums[0]>=nums[-1] and nums[0]<=x:
        #         x-=nums[0]
        #         nums.popleft()
        #         res+=1
        #     elif nums[-1]>nums[0] and nums[-1]<=x:
        #         x-=nums[-1]
        #         nums.pop
        #         res+=1

        #     if x==0: return res

        # return -1          