class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        ##### improved by Bing #####
        L=len(s)//2
        a=s[:L]
        b=s[L:]
        vowels=set("aeiouAEIOU")

        return sum(ch in vowels for ch in a)==sum(ch in vowels for ch in b)