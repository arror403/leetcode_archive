class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(substring):
            return substring == substring[::-1]
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try deleting the character at the left pointer
                without_left = s[:left] + s[left+1:]
                # Try deleting the character at the right pointer
                without_right = s[:right] + s[right+1:]
                return is_palindrome(without_left) or is_palindrome(without_right)
            
            left += 1
            right -= 1
        
        return True
        