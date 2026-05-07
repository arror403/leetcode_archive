class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        L=len(s)
        vowels="aeiouAEIOU"

        return len([i for i in s[:L//2] if i in vowels])==len([i for i in s[L//2:] if i in vowels])