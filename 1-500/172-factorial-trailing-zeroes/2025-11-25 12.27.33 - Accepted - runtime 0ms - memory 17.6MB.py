class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0: return 0

        res = 0
        k = int(log(n, 5)) + 1

        for i in range(1, k+1):
            res += n//5**i


        return res