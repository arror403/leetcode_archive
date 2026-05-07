class Solution:
    def numberOfSteps (self, num: int) -> int:
        b=0
        while(1):
            if num==0: break
            
            if num%2 == 0:
                num/=2
                b+=1
            elif num%2 == 1:
                num-=1
                b+=1
                
        return b