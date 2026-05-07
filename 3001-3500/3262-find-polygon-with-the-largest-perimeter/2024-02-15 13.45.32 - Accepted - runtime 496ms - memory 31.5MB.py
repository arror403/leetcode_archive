class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        # t=accumulate(nums)

        # print(nums)
        # print(list(t))
        prefix = sum(nums)

        for i in nums:
            prefix-=i
            if prefix>i:
                return prefix+i

        return -1