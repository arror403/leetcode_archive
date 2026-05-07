class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # n=0
        # m=0
        # for i in s3:
        #     if n<len(s1) and i==s1[n]:
        #         n+=1
        #     if m<len(s2) and i==s2[m]:
        #         m+=1
        # # print(n,m)
        # if (n+m)==len(s3) and (len(s1)+len(s2))==len(s3):
        #     return 1
        # else:
        #     return 0
        if len(s1) + len(s2) != len(s3):
            return False
        if len(s1) < len(s2):
            s1, s2 = s2, s1
        m, n = len(s1), len(s2)
        
        dp = [True] + [False] * n
        for j in range(1, n + 1):
            dp[j] = s2[j - 1] == s3[j - 1] and dp[j - 1]

        for i in range(1, m + 1):
            dp[0] = s1[i - 1] == s3[i - 1] and dp[0]
            for j in range(1, n + 1):
                dp[j] = (s1[i - 1] == s3[i + j - 1] and dp[j])
                dp[j] = dp[j] or (s2[j - 1] == s3[i + j - 1] and dp[j - 1])
        return dp[-1]