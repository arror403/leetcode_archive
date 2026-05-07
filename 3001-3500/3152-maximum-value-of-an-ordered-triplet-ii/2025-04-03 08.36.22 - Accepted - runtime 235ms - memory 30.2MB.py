class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_result = 0
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i-1], nums[i])
        
        suffix_max = [0] * n
        suffix_max[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], nums[i])
        
        for i in range(1, n-1):
            max_result = max(max_result, (prefix_max[i-1] - nums[i]) * suffix_max[i+1])
        
        
        return max_result



        # prefix_max=[]
        # suffix_max=[]
        # res=0

        # for i in range(len(nums)):
        #     prefix_max.append(max(nums[:i+1]))
        #     suffix_max.append(max(nums[i:]))

        # for i in range(1,len(nums)-1):
        #     res=max(res, (prefix_max[i-1]-nums[i])*suffix_max[i+1])


        # return res