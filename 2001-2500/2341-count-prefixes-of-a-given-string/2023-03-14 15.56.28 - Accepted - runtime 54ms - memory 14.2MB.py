class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        res=0
        for i in range(1,len(s)+1):
            print(s[:i])
            if s[:i] in words:
                res+=words.count(s[:i])

        return res