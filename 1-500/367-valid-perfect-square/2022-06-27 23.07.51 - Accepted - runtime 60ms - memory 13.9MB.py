class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        u=int(num**(0.5))

        if u**2 == num:
            return 1
        else:
            return 0