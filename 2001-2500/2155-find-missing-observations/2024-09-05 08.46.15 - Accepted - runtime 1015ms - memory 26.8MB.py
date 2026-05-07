class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total_sum = mean*(n+m)
        missing_sum = total_sum-sum(rolls)

        if missing_sum<n or missing_sum>6*n: return []
        
        base_value,remainder = divmod(missing_sum, n)
        res = [base_value]*n

        for i in range(remainder): res[i]+=1
        

        return res



# class Solution:
#     def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
#         l,s=len(rolls),sum(rolls)

#         for r in combinations_with_replacement([1,2,3,4,5,6], n):
#             if (sum(r)+s)//(l+n)==mean:
#                 return list(r)

#         return []