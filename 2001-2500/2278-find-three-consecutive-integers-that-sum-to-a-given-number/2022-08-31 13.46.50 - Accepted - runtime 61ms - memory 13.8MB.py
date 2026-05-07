class Solution:
    def sumOfThree(self, num: int) -> List[int]:
#         if num%3!=0: return []
        
#         r=num//3
        
#         return [r-1,r,r+1]
    
    
        return [] if num%3!=0 else [num//3-1,num//3,num//3+1] 