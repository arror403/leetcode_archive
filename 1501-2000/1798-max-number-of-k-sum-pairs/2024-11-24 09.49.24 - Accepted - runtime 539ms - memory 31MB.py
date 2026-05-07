class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = Counter(nums)
        res = 0
        
        # Only need to check each number once
        seen = set()
        
        for num in d:
            if num not in seen:
                # If num is half of k, handle it specially
                if num == k - num:
                    res += d[num] // 2
                else:
                    complement = k - num
                    res += min(d[num], d[complement])
                    seen.add(num)
                    seen.add(complement)
                    
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