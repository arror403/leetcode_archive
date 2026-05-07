class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return re.fullmatch('1*0*', s) != None