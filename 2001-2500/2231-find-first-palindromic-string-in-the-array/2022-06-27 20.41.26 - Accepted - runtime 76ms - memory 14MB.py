class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        f=0
        for i in words:
            if self.isPalindrome(i):
                f=1
                return i
                break
        
        if f==0:
            return ""
        
        
    def isPalindrome(self,s:str):
        return s==s[::-1]