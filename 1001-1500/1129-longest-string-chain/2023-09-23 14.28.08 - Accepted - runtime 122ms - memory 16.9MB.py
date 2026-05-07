class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # Sort the words by length
        words.sort(key=lambda x: len(x))
        
        # Initialize a dictionary to store the longest chain for each word
        dp = {}
        max_chain_length = 1
        
        for i in words:
            dp[i] = 1  # Minimum chain length is 1 (the word(i) itself)
            
            # Generate all possible predecessors of the current word
            for j in range(len(i)):
                predecessor = i[:j] + i[j+1:]
                if predecessor in dp:
                    dp[i] = max(dp[i], dp[predecessor] + 1)
            
            max_chain_length = max(max_chain_length, dp[i])
        
        return max_chain_length