class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1 = [i for i in words1 if words1.count(i) == 1]
        words2 = [i for i in words1 if words2.count(i) == 1]

        res=set(words1).intersection(set(words2))
        
        return len(list(res))