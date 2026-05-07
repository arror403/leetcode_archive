class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        L=len(nums)
        res=L
        need=cur=0
        last={0:-1}

        for v in nums: need=(need+v)%p
        
        for i in range(L):
            cur=(cur+nums[i])%p
            last[cur]=i
            want=(cur-need+p)%p

            if want in last: res=min(res, i-last[want])


        return res if res<L else -1