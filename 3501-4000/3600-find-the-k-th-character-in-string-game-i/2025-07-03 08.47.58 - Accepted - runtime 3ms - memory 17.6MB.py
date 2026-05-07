class Solution:
    def kthCharacter(self, k: int) -> str:
        m="abcdefghijklmnopqrstuvwxyz"
        i=0
        s=["a"]
        
        while i<=k:
            tmp=''.join([s[-1]]+[m[ord(c)-96] for c in s[-1]])
            s.append(tmp)
            i=len(tmp)


        return s[-1][k-1]