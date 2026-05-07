class Solution:
    def numSpecial(self, m: List[List[int]]) -> int:
        res=0
        for i,r in enumerate(m):
            if r.count(1)==0: continue
            for j,c in enumerate(zip(*m)):
                if c.count(1)==0: continue
                elif r.count(1)==c.count(1)==m[i][j]==1:
                    res+=1
        return res