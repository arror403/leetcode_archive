class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x>y: x,y=y,x
        x=list(bin(x)[2:])
        y=list(bin(y)[2:])
        for i in range(len(y)-len(x)):
            x.insert(0,'0')
        res=0
        # print(x,y)
        for i in range(len(x)):
            if x[i]!=y[i]:
                res+=1

        return res