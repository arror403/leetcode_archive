class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        count=0

        for c in s:
            if c=='(' and count>0:
                res+=c
            elif c==')' and count>1:
                res+=c

            count+=(1 if c=='(' else -1)


        return res