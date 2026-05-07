class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed=set(allowed)
        return sum(x<=allowed for x in map(set, words))