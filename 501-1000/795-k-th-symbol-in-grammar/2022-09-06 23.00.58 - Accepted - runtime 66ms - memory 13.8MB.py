class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1')&1
#         res=['0']
#         while n>0:
#             tmp=res[-1]
#             a=''
#             for i in tmp:
#                 if i == '0':
#                     a+='01'
#                 elif i == '1':
#                     a+='10'
#             res.append(a)
#             n-=1
#         print (res)
            
#         return res[-1][k-1]