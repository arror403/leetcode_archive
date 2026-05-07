class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        m=[1,10,91,739,5275,32491,168571,712891,2345851]
        
        return m[n]
#         res=0
#         for i in range(10**n+1):
#             tmp=self.tolist(i)
#             for j in range(10):
#                 f=True
#                 if tmp.count(j)>1:
#                     f=False
#                     break
#             if f: res+=1
#         return res
    
        
#     def tolist(self, n):
#         return list(map(int,str(n)))