class Solution:
    def isValid(self, word: str) -> bool:
        w=[c for c in word if c.isalpha()]
        v='aeiouAEIOU'
        
        return len(word)>=3 and word.isalnum() and any(c in v for c in w) and any(c not in v for c in w)