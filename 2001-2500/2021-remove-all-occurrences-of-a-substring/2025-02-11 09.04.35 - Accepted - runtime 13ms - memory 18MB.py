class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        x = list(s)
        m, n = len(s), len(part)
        j = 0
        
        for i in range(m):
            x[j] = s[i]
            j += 1
            if (j >= n and ''.join(x[j-n:j]) == part):
                j -= n


        return ''.join(x[:j])