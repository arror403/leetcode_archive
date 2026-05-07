class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        return list(dict.fromkeys(i for i,j in combinations(sorted(words, key=len), 2) if i in j))