class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cur=1
        pre=res=0

        for a,b in pairwise(s):
            if a==b: cur+=1
            else:
                res+=min(cur, pre)
                pre=cur
                cur=1
 

        return res + min(cur, pre)