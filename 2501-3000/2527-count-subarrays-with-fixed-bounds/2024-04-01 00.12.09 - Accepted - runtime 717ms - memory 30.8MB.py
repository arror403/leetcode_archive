class Solution:
    #ref: https://walkccc.me/LeetCode/problems/2444/
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        j = -1
        prevMinKIndex = -1
        prevMaxKIndex = -1

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                j = i
            if num == minK:
                prevMinKIndex = i
            if num == maxK:
                prevMaxKIndex = i
            # Any index k in [j + 1, min(prevMinKIndex, prevMaxKIndex)] can be the
            # start of the subarray s.t. nums[k..i] satisfies the conditions.
            ans += max(0, min(prevMinKIndex, prevMaxKIndex) - j)

        return ans





        # res=0
        # R=range(minK,maxK+1)
        # min_i=[]
        # max_i=[]
        # m=[True]*len(nums)

        # for i,v in enumerate(nums):
        #     if v==minK:
        #         min_i.append(i)
        #     if v==maxK:
        #         max_i.append(i)
        #     if v not in R:
        #         m[i]=False

        # m=[list(g) for _,g in groupby(m)]

        # print(min_i,max_i,m)
            
        # for i in min_i:
        #     for j in max_i:
        #         if i>j: continue
        #         t=nums[i:j+1]
        #         print(t)
        #         if all(x>=minK and x<=maxK for x in t):
        #             res+=1

        # return res