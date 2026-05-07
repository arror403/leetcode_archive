class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [inf]*26
        last = [0]*26
        res = 0

        for i,c in enumerate(s):
            first[ord(c)-97] = min(first[ord(c)-97], i)
            last[ord(c)-97] = i

        for i in range(26):
            if first[i] < last[i]:
                res += len(set(s[first[i]+1 : last[i]]))


        return res