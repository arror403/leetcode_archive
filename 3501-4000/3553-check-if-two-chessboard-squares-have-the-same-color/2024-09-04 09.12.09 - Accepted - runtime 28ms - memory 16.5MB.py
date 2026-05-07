class Solution:
    def checkTwoChessboards(self, c1: str, c2: str) -> bool:
        t={ord(c1[0])+int(c1[1]), ord(c2[0])+int(c2[1])}
        b={98, 100, 102, 104, 106, 108, 110, 112}
        w={99, 101, 103, 105, 107, 109, 111}


        return t<=b or t<=w