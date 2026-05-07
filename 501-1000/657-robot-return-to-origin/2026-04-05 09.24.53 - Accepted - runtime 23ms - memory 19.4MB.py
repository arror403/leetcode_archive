class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=y=0
        #d={U:DLR}
        for s in moves:
            if s=='U':y+=1
            if s=='D':y-=1
            if s=='L':x+=1
            if s=='R':x-=1

        return x==y==0