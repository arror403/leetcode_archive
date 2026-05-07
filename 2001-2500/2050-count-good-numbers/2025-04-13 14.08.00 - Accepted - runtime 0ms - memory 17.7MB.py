class Solution:
    def countGoodNumbers(self, n: int) -> int:
        e,o,M=(n+1)//2,n//2,10**9+7
        return (pow(5,e,M)*pow(4,o,M))%M