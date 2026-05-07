class Solution:
    def sumZero(self, n: int) -> List[int]:
        res=[]
        if n%2: 
            res+=[0]
            n-=1

        t=1
        while n>0:
            res+=[t,-t]
            t+=1
            n-=2


        return res 