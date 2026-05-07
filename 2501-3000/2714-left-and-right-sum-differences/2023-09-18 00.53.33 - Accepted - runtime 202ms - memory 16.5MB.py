class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return [abs(sum(nums[:i]) - sum(nums[i+1:])) for i in range(len(nums))]

        # a=nums[:]
        # a.insert(0,0)
        # a=list(itertools.accumulate(a))
        # a.pop()

        # b=nums[:]
        # b.reverse()
        # b.insert(0,0)
        # b=list(itertools.accumulate(b))
        # b.pop()
        # b.reverse()

        # return [abs(a[i]-b[i]) for i in range(len(nums))]