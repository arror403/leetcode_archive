class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        b=[1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
        # if n in b:
        #     return 1
        # else:
        #     return 0
        return n in b