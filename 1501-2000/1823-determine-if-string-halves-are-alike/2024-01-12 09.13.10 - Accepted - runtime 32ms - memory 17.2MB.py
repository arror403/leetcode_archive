class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        L=len(s)
        a=s[:L//2]
        b=s[L//2:]
        vowels="aeiouAEIOU"

        return len([i for i in a if i in vowels])==len([i for i in b if i in vowels])