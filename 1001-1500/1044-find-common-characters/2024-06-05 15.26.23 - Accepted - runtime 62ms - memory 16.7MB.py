class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d=list(map(Counter, words))
        res=[]

        for c in reduce(lambda x,y:x&y, d):
            tmp=inf
            for w in d: tmp=min(w[c],tmp)
            res+=[c]*tmp

        return res