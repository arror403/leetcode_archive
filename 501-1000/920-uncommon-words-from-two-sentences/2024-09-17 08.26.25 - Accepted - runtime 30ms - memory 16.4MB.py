class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        return [v for v,f in Counter(s1.split()+s2.split()).items() if f==1]