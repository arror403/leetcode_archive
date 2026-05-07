class Solution:
    def countOrders(self, n: int) -> int:
        return reduce(operator.mul, [1]+[comb(2*i, 2) for i in range(2, n+1)])%(10**9 + 7)