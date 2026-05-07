class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        return [j for i in words for j in i.rsplit(separator) if len(j)!=0]