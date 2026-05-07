class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer=[]
        t=0
        for i in nums:
            t = (t*2 + i)%5
            answer.append(True) if t==0 else answer.append(False)
            
        return answer
    
#         res=[]
#         for i in range(1,len(nums)+1):
#             tmp=nums[:i]
#             tmp=[str(x) for x in tmp]
#             tmp=''.join(tmp)
#             # print(tmp)
#             tmp=int(tmp,2)
#             if tmp%5 ==0:
#                 res.append(True)
#             else:
#                 res.append(False)

#         return res