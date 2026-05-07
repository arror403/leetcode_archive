class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(set(t)&set(brokenLetters)==set() for t in text.split())