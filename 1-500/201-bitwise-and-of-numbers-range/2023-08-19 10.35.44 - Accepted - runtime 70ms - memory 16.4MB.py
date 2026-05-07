class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # t=[i for i in range(left,right+1)]
        # return reduce(lambda x,y: x & y, t)
        shift = 0
        while left < right:
            left //= 2
            right //= 2
            shift += 1
        return left * (2 ** shift)