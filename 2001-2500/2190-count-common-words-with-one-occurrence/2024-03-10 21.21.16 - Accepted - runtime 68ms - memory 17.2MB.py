class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1=Counter(words1)
        d2=Counter(words2)
        res=0

        for k in d1.keys()&d2.keys():
            if d1[k]==1 and d2[k]==1:
                res+=1

        return res