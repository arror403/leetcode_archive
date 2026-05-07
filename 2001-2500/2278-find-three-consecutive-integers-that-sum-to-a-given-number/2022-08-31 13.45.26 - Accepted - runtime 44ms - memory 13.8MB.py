class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3!=0: return []
        
        r=num//3
        
        return [r-1,r,r+1]