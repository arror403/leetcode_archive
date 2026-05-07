class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
#         res=[0]*len(nums)
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i]>nums[j]:
#                     res[i]+=1
                    
#         return res
        temp = [nums[-1]] # Extra space to maintain numbers in sorted order, intially filling last element
        res = [0] # For last element, count will be always 0

        for num in nums[-2::-1]: # iterating from 2nd last to first element
            ind = bisect.bisect_left(temp, num) # Finding the correct position in temp where num will be inserted.
            temp.insert(ind, num)
            res.append(ind) # Appending in result array the ind found earlier, as it is the req. count for this num.

        return res[::-1]

