class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d=defaultdict(list)
        res=0

        for i,c in enumerate(word): d[c].append(i)
        
        word=dict.fromkeys([i for i in word if i.islower()])

        for c in word:
            u=c.upper()
            if u in d.keys():
                if all([i<d[u][0] for i in d[c]]):
                    res+=1

        return res