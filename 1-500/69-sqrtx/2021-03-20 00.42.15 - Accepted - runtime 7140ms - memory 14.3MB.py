class Solution:
    def mySqrt(self, x: int) -> int:
        b=0
        i=1
        while 1:
            
            if i**2<x:
                i+=1
                continue
            
            elif i**2>x:
                b=i-1
                break
            elif i**2==x:
                b=i
                break
                
            
        return b