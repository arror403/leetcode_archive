class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            num=self.toList(num)
            num=sum(num)
        return num
        
    
    
    
    
    def toList(self, x:int) -> List[int]:
        return list(map(int,str(x)))