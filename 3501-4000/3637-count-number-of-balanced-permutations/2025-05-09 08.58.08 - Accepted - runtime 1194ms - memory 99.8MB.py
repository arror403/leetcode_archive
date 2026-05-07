class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        d=Counter(int(c) for c in num)
        res=sum(int(c) for c in num)

        @lru_cache(maxsize=None)
        def dfs(i, odd, even, balance):
            if odd==0 and even==0 and balance==0:
                return 1
            if i<0 or odd<0 or even<0 or balance<0:
                return 0
            
            res=0
            for j in range(0, d[i]+1):
                res+=comb(odd, j)*comb(even, d[i]-j)*dfs(i-1, odd-j, even-d[i]+j, balance-i*j)
            
            return res%1000000007


        return 0 if res%2 else dfs(9, len(num)-len(num)//2, len(num)//2, res//2)