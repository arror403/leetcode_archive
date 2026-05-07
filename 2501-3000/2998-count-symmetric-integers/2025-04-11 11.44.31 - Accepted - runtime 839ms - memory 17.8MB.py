class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0

        for num in range(low, high + 1):
            s = str(num)
            if len(s) % 2 == 0:
                half = len(s) // 2
                if sum(int(digit) for digit in s[:half]) == sum(int(digit) for digit in s[half:]):
                    res += 1


        return res