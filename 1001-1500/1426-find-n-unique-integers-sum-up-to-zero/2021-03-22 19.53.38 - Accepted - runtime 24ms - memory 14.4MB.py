class Solution:
    def sumZero(self, n: int) -> List[int]:
        b=[]
        tmp=1
        if(n%2==1):
            n-=1
            b.append(0)
        for i in range(0,int(n/2)):
            b.append(tmp)
            b.append((-1)*tmp)
            tmp+=1
        return b