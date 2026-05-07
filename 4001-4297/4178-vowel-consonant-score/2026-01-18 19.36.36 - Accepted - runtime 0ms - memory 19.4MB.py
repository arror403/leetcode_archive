class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        v=c=0
        for x in s:
            if x in 'aeiou':
                v+=1
            elif x.isalpha():
                c+=1

        return v//c if c else 0