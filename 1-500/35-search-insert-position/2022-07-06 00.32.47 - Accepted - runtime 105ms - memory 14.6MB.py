class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # if len(nums)==1:
        #     if nums[0]<=target:
        #         return 0
        #     else:
        #         return 1
        # else:
        #     if target<nums[0]:
        #         return 0
        #     elif target>nums[-1]:
        #         return len(nums)
        #     else:
        #         for i in range(len(nums)-1):
        #             if target>nums[i] and target<=nums[i+1]:
        #                 return i+1

        l , r = 0, len(nums)-1
        while l <= r:
            mid=int((l+r)/2)
            if nums[mid]== target:
                return mid
            if nums[mid] < target:
                l = mid+1
            else:
                r = mid-1
        return l