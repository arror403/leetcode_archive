class Solution:
    def countSubstrings(self, s: str) -> int:
        t = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
        res=0

        for i in t:
            if i==i[::-1]:
                res+=1

        return res