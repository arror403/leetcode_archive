class Solution:
    def stringHash(self, s: str, k: int) -> str:
        def util(x): return chr((sum(ord(c)-97 for c in x)%26)+97)

        return ''.join(map(util, [s[i:i+k] for i in range(0, len(s), k)]))