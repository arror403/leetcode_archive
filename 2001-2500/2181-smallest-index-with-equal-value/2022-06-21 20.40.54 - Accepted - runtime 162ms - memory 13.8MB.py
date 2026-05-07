class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        flag=0
        for i in range(len(nums)):
            if i%10 == nums[i]:
                flag=1
                return i
                break
        if flag == 0:
            return -1