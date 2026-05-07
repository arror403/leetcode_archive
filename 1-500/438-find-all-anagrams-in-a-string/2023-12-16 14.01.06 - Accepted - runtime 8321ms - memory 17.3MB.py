class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l_p=len(p)
        l_s=len(s)
        p=Counter(p)
        
        res=[]

        for i in range(l_s):
            if Counter(s[i:i+l_p])==p:
                res.append(i)

        return res