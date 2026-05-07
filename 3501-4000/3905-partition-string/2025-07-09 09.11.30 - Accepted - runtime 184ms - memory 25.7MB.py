class Solution:
    def partitionString(self, s: str) -> List[str]:
        seen=set()
        res=[]

        i=0
        for j in range(1, len(s)+1):
            t=s[i:j]
            if t not in seen:
                res.append(t)
                seen.add(t)
                i=j


        return res