class Solution:
    ##### power by chatGPT #####
    def findMaxLength(self, nums: List[int]) -> int:
        max_length=0
        sum_map={0:-1}  # Mapping the running sum to its index, initialized with 0 at index -1
        curr_sum=0
        
        for i in range(len(nums)):
            if nums[i]==0:
                curr_sum-=1
            else:
                curr_sum+=1
                
            if curr_sum in sum_map:
                max_length=max(max_length, i-sum_map[curr_sum])
            else:
                sum_map[curr_sum]=i
        
        return max_length