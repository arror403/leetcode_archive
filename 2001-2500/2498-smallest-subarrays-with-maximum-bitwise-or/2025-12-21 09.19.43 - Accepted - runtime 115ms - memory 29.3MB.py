class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        L = len(nums)
        res = [1]*L

        for i in range(L):
            # res[i] = 1
            j = i-1
            while j>=0 and (nums[i] | nums[j]) != nums[j]:
                res[j] = i-j+1
                nums[j] |= nums[i]
                j -= 1


        return res