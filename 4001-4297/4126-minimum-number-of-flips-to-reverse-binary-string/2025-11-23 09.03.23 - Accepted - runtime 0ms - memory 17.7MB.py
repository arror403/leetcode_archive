class Solution:
    def minimumFlips(self, n: int) -> int:
        b=bin(n)[2:]

        return sum(int(xor(int(x), int(y))) for x, y in zip(b, b[::-1]))