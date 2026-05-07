class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def countUglyNumbers(x, a, b, c):
            return x // a + x // b + x // c - x // math.lcm(a, b) - x // math.lcm(b, c) - x // math.lcm(a, c) + x // math.lcm(a, math.lcm(b, c))

        left = 1
        right = 2 * (10**9)  # Set an arbitrary upper limit for binary search
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            count = countUglyNumbers(mid, a, b, c)

            if count >= n:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result