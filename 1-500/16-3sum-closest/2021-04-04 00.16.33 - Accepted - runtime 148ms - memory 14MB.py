class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
        
        
#         b=[]
#         x=0
#         min=9999
#         if len(nums)==3: return sum(nums)
        
#         else:
#             nums.sort()
#             # print (nums)
#             for i in range(len(nums)-2):
#                 for j in range(i+1,len(nums)-1):
#                     for k in range(j+1,len(nums)):
#                         tmp=nums[i]+nums[j]+nums[k]
#                         if not(tmp in b): b.append(tmp)
#                         # b.append(tmp)

#             b.sort()
#             for i in b:
#                 if abs(target-i)<min:
#                     min=abs(target-i)
#                     x=i

#             # print (b)
        
#             return x