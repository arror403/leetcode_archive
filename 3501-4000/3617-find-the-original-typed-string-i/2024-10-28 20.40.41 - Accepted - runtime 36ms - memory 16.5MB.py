class Solution:
    def possibleStringCount(self, word: str) -> int:
        res=1
        t=[list(g) for _,g in groupby(word)]
        
        for c in t:
            if len(c)>1:
                res+=(len(c)-1)

        
        return res