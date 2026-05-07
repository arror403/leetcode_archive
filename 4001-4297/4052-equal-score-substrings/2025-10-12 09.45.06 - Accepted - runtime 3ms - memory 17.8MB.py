class Solution:
    def scoreBalance(self, s: str) -> bool:
        m = [ord(c)-96 for c in s]
        l = m[0]
        r = sum(m) - l

        for i in range(1, len(s)):
            if l == r: return True
            l += m[i]
            r -= m[i]

        return False