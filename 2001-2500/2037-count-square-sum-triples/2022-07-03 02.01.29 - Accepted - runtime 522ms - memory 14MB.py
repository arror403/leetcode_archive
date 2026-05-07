class Solution:
    def countTriples(self, n: int) -> int:
#         t=0
#         b=[5,13,17,25,29,37,41,53,61,65,65,73,85,85,89,97,
# 101,109,113,125,137,145,145,149,157,169,173,181,185,185,
# 193,197,205,205,221,221,229,233,241]
        
#         for i in b:
#             tmp=1
#             while (tmp*i) <= n:
#                 tmp+=1
#                 t+=2
                
#         return t
        t=0
        for i in range(1,n):
            for j in range(i+1,n+1):
                s=(i*i+j*j)**(0.5)
                if int(s)==s and s<=n:
                    t+=2
        return t