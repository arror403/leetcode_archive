class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         for x, k in queries:
#             if A[k] % 2 == 0: S -= A[k]
#             A[k] += x
#             if A[k] % 2 == 0: S += A[k]
#             ans.append(S)

        # return ans
        res,s=[],0
        for i in nums:
            if i%2==0:
                s+=i
                
        for i in queries:
            if nums[i[1]]%2==0: s-=nums[i[1]]
            nums[i[1]]+=i[0]
            if nums[i[1]]%2==0: s+=nums[i[1]]
            res.append(s)
                
        return res