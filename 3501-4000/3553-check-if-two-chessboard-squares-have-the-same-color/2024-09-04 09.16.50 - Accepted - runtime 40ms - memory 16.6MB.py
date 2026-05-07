class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        return (ord(c1[0])+int(c1[1])+ord(c2[0])+int(c2[1]))%2==0