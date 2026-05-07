class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(maxsize=None)
        def sub(a, b, i, j):
            n, m = len(a), len(b)
            S = 0

            if i == n or j == m:
                if i == n and j == m: 
                    return 0
                if i == n:
                    return sum(ord(b[x]) for x in range(j, len(b)))
                else:
                    return sum(ord(a[x]) for x in range(i, len(a)))
    
            if a[i] == b[j]:
                S = sub(a, b, i+1, j+1)
            else:
                S = min(sub(a, b, i+1, j) + ord(a[i]),
                        sub(a, b, i, j+1) + ord(b[j]))
            
            return S


        return sub(s1, s2, 0, 0)