class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n=len(nums)
        k=n-2
        l=n-1

        while k>=0:
            if nums[k]<nums[k+1]:
                break
            k-=1

        if k<0:
            nums.reverse()
        else:
            while l>k:
                if nums[l]>nums[k]:
                    break
                l-=1

            nums[k],nums[l]=nums[l],nums[k]
            # Sort the suffix instead of just reversing
            left, right = k + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1