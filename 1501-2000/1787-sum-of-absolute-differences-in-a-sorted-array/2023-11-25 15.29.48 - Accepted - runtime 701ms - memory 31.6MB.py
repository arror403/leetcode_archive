class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total_sum = sum(nums)
        prefix_sum = 0
        result = []
        l=len(nums)

        for i,v in enumerate(nums):
            result.append((total_sum - prefix_sum) - v*l + i*v*2 - prefix_sum)
            prefix_sum += v

        return result
        # res=[]

        # l=len(nums)

        # for i,v in enumerate(nums):
        #     res.append(sum(nums[i:])-(l-i)*v + i*v-sum(nums[:i]))

        # return res