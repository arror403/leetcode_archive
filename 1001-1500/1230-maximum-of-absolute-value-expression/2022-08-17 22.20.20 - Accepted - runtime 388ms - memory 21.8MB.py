class Solution:
    def maxAbsValExpr(self, x: List[int], y: List[int]) -> int:
        res= 0
        for p, q in [[1,1], [1,-1], [-1,1], [-1,-1]]:
            smallest = p*x[0] + q*y[0]
            for i in range(len(x)):
                cur = p*x[i] + q*y[i] + i
                res = max(res, cur-smallest)
                smallest = min(smallest, cur)
        return res        
        
        

#         res=-inf
#         for i in range(len(arr1)):
#             for j in range(i+1,len(arr1)):
#                 tmp=abs(arr1[i]-arr1[j])+abs(arr2[i]-arr2[j])+abs(i-j)
#                 if tmp>res: res=tmp

                    
#         return res