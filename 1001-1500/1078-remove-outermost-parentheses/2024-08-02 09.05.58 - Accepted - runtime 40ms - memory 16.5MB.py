class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=tmp=""
        q=0

        for x in s:
            if x=='(':
                tmp+=x 
                q+=1
            else:
                tmp+=x
                q-=1

            if q==0:
                res+=tmp[1:-1]
                tmp=""

        return res