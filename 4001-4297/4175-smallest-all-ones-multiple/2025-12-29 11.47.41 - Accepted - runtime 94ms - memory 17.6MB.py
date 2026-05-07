class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k%2==0 or k%5==0: return -1

        r = 1%k
        res = 1
        while r != 0:
            r = (r*10 + 1) % k
            res += 1

        return res