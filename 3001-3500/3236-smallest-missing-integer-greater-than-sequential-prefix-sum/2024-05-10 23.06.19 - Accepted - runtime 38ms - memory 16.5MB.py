class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        L=len(nums)
        i=0
        res=nums[i]

        while (i+1)<L and nums[i+1]==nums[i]+1:
            res+=nums[i+1]
            i+=1

        if res not in nums:
            return res
        else:
            while res in nums: res+=1
            return res     

        



        # n=nums[:]
        # g=[]
        # res=[]

        # while nums:
        #     L=len(nums)
        #     i=0
        #     tmp=[nums[i]]

        #     while (i+1)<L and nums[i+1]==nums[i]+1:
        #         tmp.append(nums[i+1])
        #         i+=1

        #     g.append(tmp)
        #     nums=nums[i+1:]

        # g.sort(key=len, reverse=True)

        # M=len(g[0])

        # for i in g:
        #     if len(i)==M:
        #         tmp=sum(i)
        #         if tmp not in n:
        #             res.append(tmp)
        #         else:
        #             while tmp in n: tmp+=1
        #             res.append(tmp)
        #     else:
        #         break


        # return min(res)