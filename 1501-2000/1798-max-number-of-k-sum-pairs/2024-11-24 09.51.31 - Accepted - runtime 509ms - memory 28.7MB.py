class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0
        
        while l < r:
            current_sum = nums[l] + nums[r]
            if current_sum == k:
                res += 1
                l += 1
                r -= 1
            elif current_sum < k:
                l += 1
            else:
                r -= 1
                

        return res



        # d=Counter([n%k for n in nums if n<k])
        # res=0

        # t=1
        # q,r=divmod(k,2)
        # if r==1:
        #     for _ in range(q):
        #         res+=min(d[t], d[k-t])
        #         t+=1
        # else:
        #     for _ in range(q-1):
        #         res+=min(d[t], d[k-t])
        #         t+=1            

        #     res+=d[q]//2


        # return res