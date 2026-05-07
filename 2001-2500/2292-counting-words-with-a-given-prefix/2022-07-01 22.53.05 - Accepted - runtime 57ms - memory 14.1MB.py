class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        t=0
        [list(i) for i in words]
        # print(words)
        pref=list(pref)
        # print(pref)
        for i in words:
            if len(i)<len(pref):
                continue
            else:
                f=1
                for k in range(len(pref)):
                    if i[k]!=pref[k]:
                        f=0
                        break
                if f:
                    t+=1
                    
        return t
            