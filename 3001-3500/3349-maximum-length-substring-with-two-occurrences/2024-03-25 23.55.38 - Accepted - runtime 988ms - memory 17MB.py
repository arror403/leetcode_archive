class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res=[]
        L=len(s)
        t=[s[i:j] for i in range(L) for j in range(i+1,L+1)]

        for x in t:
            if all([v<=2 for v in Counter(x).values()]):
                res.append(x)

        return len(max(res,key=len))