class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((i for i in words if i==i[::-1]),"")