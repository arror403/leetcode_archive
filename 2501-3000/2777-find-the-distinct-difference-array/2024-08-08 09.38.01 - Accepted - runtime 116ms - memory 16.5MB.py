class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        def dist_len(arr): return len(dict.fromkeys(arr))
        # res=[]

        # for i in range(len(nums)):
        #     if i==0:
        #         res.append(1-dist_len(nums[1:]))
        #     else:
        #         res.append(dist_len(nums[:i+1])-dist_len(nums[i+1:]))

        return [1-dist_len(nums[1:]) if i==0 else dist_len(nums[:i+1])-dist_len(nums[i+1:]) for i in range(len(nums))]

        # return res