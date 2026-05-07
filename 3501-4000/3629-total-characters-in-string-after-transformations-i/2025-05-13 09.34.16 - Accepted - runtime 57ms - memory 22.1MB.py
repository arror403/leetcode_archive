dp=[1]*(100_026)
for i in range(26, 100_026): dp[i] = (dp[i-26]+dp[i-25])%1_000_000_007

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        res=0
        for v,f in Counter(s).items():
            res=(res+f*dp[(ord(v)-97)+t])%1_000_000_007
        
        return res