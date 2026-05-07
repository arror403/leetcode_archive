class Solution:
    def maxFreqSum(self, s: str) -> int:
        a,b=[0],[0]
        
        for c,f in Counter(s).items():
            if c in "aeiou": a.append(f)
            else: b.append(f)

        
        return max(a)+max(b)