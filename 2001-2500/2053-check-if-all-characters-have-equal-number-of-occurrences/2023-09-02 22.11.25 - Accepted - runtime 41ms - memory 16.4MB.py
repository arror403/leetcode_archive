class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        t=dict.fromkeys(list(s),0)
        for i in s: t[i]+=1
        return len(set(list(t.values())))==1
