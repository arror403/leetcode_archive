class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # Use boolean array instead of set for tracking middle chars
        # saves space especially for very long strings
        first = {}
        last = {}
        result = 0
        
        # Get first and last positions
        for i, c in enumerate(s):
            if c not in first:
                first[c] = i
            last[c] = i
            
        # For each unique outer character
        for c in first:
            if last[c] - first[c] >= 2:
                # Use boolean array instead of set
                seen = [False] * 26
                # Mark all chars between first and last occurrence
                for i in range(first[c] + 1, last[c]):
                    seen[ord(s[i]) - ord('a')] = True
                # Count unique middle chars
                result += sum(seen)
                
        return result