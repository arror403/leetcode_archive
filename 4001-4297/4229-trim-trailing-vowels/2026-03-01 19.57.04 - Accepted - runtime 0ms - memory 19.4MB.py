class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        res=list(s)
        while res and (res[-1] in "aeiou"): res.pop()
        return ''.join(res)