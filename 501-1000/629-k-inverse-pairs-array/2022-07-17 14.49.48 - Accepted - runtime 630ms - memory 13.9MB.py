class Solution:
    def kInversePairs(self, N: int, K: int) -> int:
#         1000000007
        ds = [0] + [1] * (K + 1)
        for n in range(2, N+1):
            new = [0]
            for k in range(K+1):
                v = ds[k+1]
                v -= ds[k-n+1] if k >= n else 0
                new.append( (new[-1] + v) % 1000000007 )
            ds = new
        return (ds[K+1] - ds[K]) % 1000000007        