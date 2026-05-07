class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # Two-pointer approach
        left = zeros = max_length = 0
        
        for right in range(len(nums)):
            if nums[right] == 0: zeros += 1

            # Shrink window if more than one zero
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # Update max length (current window length - 1 for deleted element)
            max_length = max(max_length, right - left)
        
        # If all 1s, return length - 1
        return min(max_length, len(nums) - 1)



        # m=[[k,len(list(g))] for k,g in groupby(nums)]
        # res=t=ind=0
        # for i in range(1,len(m)-1):
        #     ind+=m[i-1][1]
        #     if m[i-1][0]==m[i+1][0]==1 and m[i][0]==0:
        #         if (tmp:=m[i-1][1]+m[i+1][1]+1)>t:
        #             t=tmp
        #             res=ind
        # return res if res!=0 else 0