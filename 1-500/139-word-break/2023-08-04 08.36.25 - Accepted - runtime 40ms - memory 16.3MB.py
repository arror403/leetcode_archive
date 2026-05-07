class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                word_len = len(word)
                if i >= word_len and s[i - word_len:i] == word:
                    dp[i] = dp[i] or dp[i - word_len]

        return dp[n]