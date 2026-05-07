class Solution:
    def findMaxForm(self, strs: List[str], zeros: int, ones: int) -> int:
        dp = [[0]*(zeros+1) for _ in range(ones+1)]

        for s in strs:
            currOnes = s.count('1')
            currZeros = len(s)-currOnes
            
            for j in range(ones, currOnes-1, -1):
                for i in range(zeros, currZeros-1, -1):
                    dp[j][i] = max(dp[j][i], 1 + dp[j-currOnes][i-currZeros])
                    # dp[i][j] = max(dp[i][j], 1 + dp[i-currZeros][j-currOnes])
                
        
        return dp[-1][-1]