class Solution:
    def minOperations(self, s: str) -> int:

        ##### power by chatGPT #####

        L = len(s)
        a, b = 0, 0

        for i in range(L):
            if i % 2 == 0 and s[i] != '0':
                a += 1
            elif i % 2 == 1 and s[i] != '1':
                a += 1

            if i % 2 == 0 and s[i] != '1':
                b += 1
            elif i % 2 == 1 and s[i] != '0':
                b += 1

        return min(a, b)