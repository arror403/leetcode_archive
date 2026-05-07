class Solution:
    def countOdds(self, low: int, high: int) -> int:
#         b=0
#         for i in range(low,high+1):
#             if i%2==1:
#                 b+=1
                
#         return b
        if low%2==0:
            low+=1
        if high%2==0:
            high-=1
            
        return int((high-low)/2+1)