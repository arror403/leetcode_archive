class Solution:
    def checkPossibility(self, N: List[int]) -> bool:
        err = 0
        for i in range(1, len(N)):
            if N[i] < N[i-1]:
                if err or (i > 1 and i < len(N) - 1 and N[i-2] > N[i] and N[i+1] < N[i-1]):
                    return False
                err = 1
        return True
#         f=True
#         for i in range(1,len(nums)):
#             tmp=list(nums)
#             if tmp[i-1]<=tmp[i]:
#                 continue
#             else:
#                 tmp[i]=tmp[i-1]
#                 if self.nonDecreasing(tmp):
#                     continue
#                 else:
#                     f=False
#                     break
                    
#         return f
    
    
#     def nonDecreasing(self,l):
#         f=True
#         for i in range(len(l)-1):
#             if l[i]<=l[i+1]:
#                 continue
#             else:
#                 f=False
#                 break
#         return f   