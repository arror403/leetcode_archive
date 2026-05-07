class Solution:
    def possibleStringCount(self, word: str) -> int:
        return sum(len(list(g))-1 for _,g in groupby(word))+1