class Solution:
    def longestPalindrome(self, s: str) -> int:
        return len(s) if (x:=len([f for f in Counter(s).values() if f%2==1]))==0 else len(s)-x+1