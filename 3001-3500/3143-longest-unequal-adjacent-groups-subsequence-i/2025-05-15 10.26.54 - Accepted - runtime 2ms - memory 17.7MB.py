class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        target = len(words)
        if target == 1: return words
        memo = {0:(groups[0],[words[0]])}

        for i in range(1, target):
            group, letter = memo[i-1]
            if groups[i] != group:
                memo[i] = (groups[i], letter + [words[i]])
            else:
                memo[i] = (group, letter)
        
        
        return memo[target - 1][1]