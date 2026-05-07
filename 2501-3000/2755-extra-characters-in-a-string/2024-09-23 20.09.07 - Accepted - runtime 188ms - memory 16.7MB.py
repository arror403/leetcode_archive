class Solution:
    def minExtraChar(self, s: str, d: List[str]) -> int:
        dp=[-1]*51

        def Helper(s, d, i):
            nonlocal dp
            if i==len(s): return 0

            if dp[i]==-1:
                dp[i] = Helper(s, d, i+1) + 1

                for w in d:
                    if s[i:i+len(w)]==w:
                        dp[i] = min( dp[i], Helper(s, d, i+len(w)) )

            return dp[i]


        return Helper(s, d, 0)