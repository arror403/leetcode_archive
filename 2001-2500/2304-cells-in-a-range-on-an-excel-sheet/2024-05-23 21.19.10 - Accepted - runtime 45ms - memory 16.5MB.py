class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        return [chr(c)+str(i) for c in range(ord(s[0]),ord(s[3])+1) for i in range(int(s[1]),int(s[4])+1)]