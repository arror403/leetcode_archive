class Solution:
    def numberOfSteps(self, num: int) -> int:
        t=0
        while num!=0:
            if num%2==0:
                num/=2
                t+=1
            else:
                num-=1
                t+=1
        return t