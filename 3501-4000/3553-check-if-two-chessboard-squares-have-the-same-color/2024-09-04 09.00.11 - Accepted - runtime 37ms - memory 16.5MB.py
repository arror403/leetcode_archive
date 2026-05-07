class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        b=[c+i for c in "aceg" for i in "1357"]+[c+i for c in "bdfh" for i in "2468"]
        w=[c+i for c in "aceg" for i in "2468"]+[c+i for c in "bdfh" for i in "1357"]

        return (coordinate1 in b and coordinate2 in b) or (coordinate1 in w and coordinate2 in w)