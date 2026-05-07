class Solution:
    def residuePrefixes(self, s: str) -> int:
        return len([i for i in range(1,len(s)+1) if len(set(s[:i]))==i%3])