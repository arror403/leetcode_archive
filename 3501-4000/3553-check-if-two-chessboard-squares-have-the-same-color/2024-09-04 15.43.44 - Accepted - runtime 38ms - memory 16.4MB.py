class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        def util(p): return (ord(p[0])+int(p[1]))%2
        
        return util(c1)==util(c2)