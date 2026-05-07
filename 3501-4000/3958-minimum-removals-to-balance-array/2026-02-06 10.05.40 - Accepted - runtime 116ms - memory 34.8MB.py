class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        L=len(nums)
        nums.sort()
        ms=0
        l=0

        for r in range(L):
            while nums[r] > k*nums[l]:
                l+=1
            ms=max(ms, r-l+1)


        return L-ms

        # t=sorted(set(nums))
        # s=set()
        # for x in t:
        #     p=bisect_left(nums,x*k)
        #     s.add(L-p)

        # print(s)
        # return 0