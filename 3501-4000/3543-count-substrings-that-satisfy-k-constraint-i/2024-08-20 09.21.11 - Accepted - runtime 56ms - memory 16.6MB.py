class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        L=len(s)
        res=0
        for i in range(L):
            zeros=ones=0
            for j in range(i, L):
                if s[j]=='0': zeros+=1
                else: ones+=1

                if zeros<=k or ones<=k: res+=1

        return res