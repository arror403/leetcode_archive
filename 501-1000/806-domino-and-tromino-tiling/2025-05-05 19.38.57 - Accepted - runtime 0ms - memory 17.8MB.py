class Solution:
    def numTilings(self, n: int) -> int:
        v=[0]*1001
        v[1],v[2],v[3]=1,2,5
        m=10**9+7

        if n<=3: return v[n]

        for i in range(4, n+1): v[i]=(2*v[i-1]+v[i-3])%m


        return v[n]