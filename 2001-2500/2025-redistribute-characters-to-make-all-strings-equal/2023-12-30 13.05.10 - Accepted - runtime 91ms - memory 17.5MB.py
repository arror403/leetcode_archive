class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        L=len(words)
        words=''.join(words)
        t=Counter(words)
        for x in t.values():
            if x%L!=0:
                return False

        return True