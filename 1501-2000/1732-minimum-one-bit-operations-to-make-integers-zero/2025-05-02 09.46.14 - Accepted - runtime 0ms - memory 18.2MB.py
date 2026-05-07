class Solution:
    dp={0:0}
    def minimumOneBitOperations(self, n: int) -> int:
        if n not in self.dp:
            b=1
            while (b<<1)<=n: b<<=1
            self.dp[n]=self.minimumOneBitOperations((b>>1)^b^n)+b

        return self.dp[n]