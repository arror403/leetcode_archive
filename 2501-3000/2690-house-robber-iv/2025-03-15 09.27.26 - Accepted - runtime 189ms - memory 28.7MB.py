class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        left,right=min(nums),max(nums)

        while left<right:
            mid=(left+right)//2
            last=take=0
            for v in nums:
                if last:
                    last=0
                    continue
                if v<=mid:
                    take+=1
                    last=1

            if take>=k:
                right=mid
            else:
                left=mid+1


        return left