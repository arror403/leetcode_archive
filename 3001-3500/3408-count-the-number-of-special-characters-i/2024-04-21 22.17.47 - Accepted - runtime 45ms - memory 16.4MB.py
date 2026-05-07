class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        return sum(1 for c in set(word) if chr(ord(c)-32) in set(word))