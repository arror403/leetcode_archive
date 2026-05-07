class Solution:
    def maxFreqSum(self, s: str) -> int:
        a=b=0
        
        for c,f in Counter(s).items():
            if c in 'aeiou': a=max(a,f)
            else: b=max(b,f)

        
        return a+b