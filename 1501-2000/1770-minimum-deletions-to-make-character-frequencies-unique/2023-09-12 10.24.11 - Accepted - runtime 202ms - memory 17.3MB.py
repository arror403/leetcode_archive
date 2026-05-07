class Solution:
    def minDeletions(self, s: str) -> int:
        t=dict.fromkeys(s,0)
        for i in s: t[i]+=1
        # print(t)
        t=[v for k,v in t.items()]
        res=0
        # print(t)
        while len(set(t))!=len(t):
            t=[x for x in t if x>0]
            for i in range(len(t)):
                if t.count(t[i])>1:
                    t[i]-=1
                    res+=1

        # print(t)

        return res