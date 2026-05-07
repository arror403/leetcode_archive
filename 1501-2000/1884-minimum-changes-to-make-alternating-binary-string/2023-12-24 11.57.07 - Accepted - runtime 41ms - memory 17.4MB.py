class Solution:
    def minOperations(self, s: str) -> int:
        L=len(s)
        t=self.bin_util(L)
        a,b=0,0
        for i,v in enumerate(s):
            if t[0][i]!=v: a+=1
            if t[1][i]!=v: b+=1

        return min(a,b)



    def bin_util(self, length): # generate_alternating_patterns
        pattern_01 = "01" * (length // 2)
        pattern_10 = "10" * (length // 2)
        
        # Adjust for odd length
        if length % 2 == 1:
            pattern_01 += "0"
            pattern_10 += "1"
        
        return [pattern_01, pattern_10]