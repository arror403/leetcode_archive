class Solution:
    def countDigitOne(self, n: int) -> int:
        if n==0: return 0

        res = 0
        i = 1

        while i <= n:
            divider = i * 10
            res += (n // divider) * i  # Full cycles
            remaining = n % divider
            if remaining >= i:
                res += min(max(remaining - i + 1, 0), i)  # Partial cycle
            # print(divider, remaining, i, res)
            i *= 10

        return res