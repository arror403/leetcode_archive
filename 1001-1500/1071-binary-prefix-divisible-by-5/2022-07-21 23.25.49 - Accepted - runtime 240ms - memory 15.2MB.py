class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer=[]
        num=0
        for i in range(len(nums)):
            num = (num*2 + nums[i])%5
            answer.append(True) if num==0 else answer.append(False)
            
        return answer
    
    
        # for(int i=0; i<a.size(); i++)
        # {
        #     num = (num*2 + a[i])%5;
        #     answer.push_back(num==0);
        # }
        # return answer;
    
    
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