class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return sum(1 for word in words if all(char in allowed for char in word))