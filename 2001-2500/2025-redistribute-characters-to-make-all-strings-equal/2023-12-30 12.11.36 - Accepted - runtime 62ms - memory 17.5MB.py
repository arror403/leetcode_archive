class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return all(x%len(words)==0 for x in Counter(''.join(words)).values())