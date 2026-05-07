class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        
        for length in range(1, n // 2 + 1):
            if n % length == 0:
                substring = s[:length]
                times = n // length
                constructed_string = substring * times
                
                if constructed_string == s:
                    return True
        
        return False