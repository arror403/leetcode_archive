class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        L = len(s)
        res = [0]*L
        pre = -L

        for i in range(L):
            if s[i] == c:
                pre = i
            res[i] = i-pre

        for i in range(pre-1, -1, -1):
            if s[i] == c:
                pre = i
            res[i] = min(res[i], pre-i)


        return res