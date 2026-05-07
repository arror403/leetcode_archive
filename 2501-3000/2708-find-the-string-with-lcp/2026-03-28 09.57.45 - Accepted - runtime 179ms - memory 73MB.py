class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        L = len(lcp)
        res = [0] * L
        c = 1

        for i in range(L):
            if res[i]: 
                continue
            if c > 26: 
                return ''
            for j in range(i, L):
                if lcp[i][j]:
                    res[j] = c
            c += 1
            
        for i in range(L):
            for j in range(L):
                v = lcp[i + 1][j + 1] if i + 1 < L and j + 1 < L else 0
                v = v + 1 if res[i] == res[j] else 0
                if lcp[i][j] != v:
                    return ''


        return ''.join(chr(96 + i) for i in res)