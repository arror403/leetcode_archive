class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         d,t={},0
#         nums=[int(x) for x in nums]
#         for i in list(dict.fromkeys(nums)): d[i]=0
            
#         for i in nums: d[i]+=1
            
#         d=dict(sorted(d.items(), key=lambda x: x[0], reverse=True))
        
#         # print(d)
#         for i in d:
#             t+=d[i]
#             if k<=t: return str(i)
            return str(sorted([int(x) for x in nums])[len(nums)-k])
            
