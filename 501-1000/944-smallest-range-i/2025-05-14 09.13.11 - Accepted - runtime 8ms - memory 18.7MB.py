class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        mx = mn = nums[0]
        for v in nums: mx, mn = max(mx, v), min(mn, v)
        
        return max(0, mx-mn-2*k)


        # ave=round(sum(nums)/len(nums))
        # m=[]

        # for v in nums:
        #     if abs(v-ave)>k:
        #         m.append(abs(v-k))
        #     else:
        #         m.append(ave)


        # return max(m)-min(m)