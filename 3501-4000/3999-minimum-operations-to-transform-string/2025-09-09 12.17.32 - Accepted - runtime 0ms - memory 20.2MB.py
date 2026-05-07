class Solution:
    def minOperations(self, s: str) -> int:
        h="abcdefghijklmnopqrstuvwxyz"

        for i in range(1, 26):
            if h[i] in s: 
                return 26-i


        return 0