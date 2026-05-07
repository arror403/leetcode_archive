class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0:
            return "0"
        result = []
        while N != 0:
            remainder = N % (-2)
            N //= (-2)
            if remainder < 0:
                remainder += 2
                N += 1
            result.append(str(remainder))
        result.reverse()
        return ''.join(result)