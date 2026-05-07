class Solution:
    def getSmallestString(self, s: str) -> str:
        res=[s]

        for i in range(len(s)-1):
            t=list(s)

            if int(t[i])%2==int(t[i+1])%2:
                t[i],t[i+1]=t[i+1],t[i]
                res.append(''.join(t))

        # print(res)
        return min(res)