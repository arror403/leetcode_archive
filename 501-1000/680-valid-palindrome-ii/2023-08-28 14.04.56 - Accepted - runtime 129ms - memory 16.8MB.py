class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Check if removing s[left] or s[right] leads to a palindrome
                return self.isp(s, left + 1, right) or self.isp(s, left, right - 1)
            left += 1
            right -= 1
        
        return True
    
    def isp(self, t, start, end):
        while start < end:
            if t[start] != t[end]:
                return False
            start += 1
            end -= 1
        return True
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         s=list(s)

#         if self.isp(s): return True

#         tmp=[]

#         for i in range(len(s)):
#             tmp=s[:]
#             tmp.pop(i)
#             if self.isp(tmp): return True

#         return False

#     def isp(self, t):
#         return t==t[::-1]
        