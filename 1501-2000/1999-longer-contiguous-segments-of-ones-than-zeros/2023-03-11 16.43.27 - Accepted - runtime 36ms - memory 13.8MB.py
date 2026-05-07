class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        res = [list(y) for x, y in groupby(s)]
        # print (res)
        a,b=0,0
        for i in res:
            if i[0]=='0' and len(i)>b : b=len(i)
            elif len(i)>a :a=len(i)
        # return 0
        return a>b
