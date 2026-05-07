class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if re.search(p,s)==None: return False
        else: return s==re.search(p,s).group(0)