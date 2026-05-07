class Solution:
    def numberOfWays(self, a: int, b: int, k: int) -> int:
        return 0 if (abs(b-a)+k)%2==1 else comb(k,(abs(b-a)+k)//2)%(10**9+7)