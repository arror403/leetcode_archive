class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        L=len(s)
        res=[]

        for i in range(0, L, k):
            if i+k<L:
                res.append(s[i:i+k])
            else:
                tmp=s[i:]
                res.append(tmp+fill*(k-len(tmp)))


        return res