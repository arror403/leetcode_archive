class Solution:
    def totalMoney(self, n: int) -> int:
        r,res=0,0
        while 1:
            if n>=7:
                res+=(r+4)*7
                r+=1
                n-=7
            else:
                res+=(2*r+1+n)*n//2
                break

        return res