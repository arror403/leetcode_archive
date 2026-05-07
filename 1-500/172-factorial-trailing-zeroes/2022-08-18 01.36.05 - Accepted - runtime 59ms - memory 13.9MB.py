class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n==0: return 0
        k,res=int(math.log(n,5)),0
        for i in range(1,k+1): res+=int(n/(5**i))
        return res