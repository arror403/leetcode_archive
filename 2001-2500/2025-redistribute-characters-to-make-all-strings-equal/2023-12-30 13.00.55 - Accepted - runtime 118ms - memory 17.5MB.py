class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        return next((x for x in Counter(''.join(words)).values() if x%len(words)!=0),None)==None