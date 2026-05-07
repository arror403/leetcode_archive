class Solution:
    def makeFancyString(self, s: str) -> str:
        res=""

        for k,g in groupby(s):
            l=len(list(g))

            if l<=2:
                res+=k*l
            else:
                res+=k*2


        return res