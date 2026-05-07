class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        min_r = inf
        max_r = -inf

        def dfs(l, r, n, R):
            nonlocal min_r
            nonlocal max_r
            
            if l==r:
                min_r = min(min_r, R)
                max_r = max(max_r, R)
            else:
                if l>r:
                    l,r=r,l
                for i in range(1, l+1):
                    j=l-i+1
                    while i+j <= min(r, (n+1)//2):
                        if l+r-(i+j) <= n//2:
                            dfs(i, j, (n+1)//2, R+1)
                        j+=1


        dfs(firstPlayer, n-secondPlayer+1, n, 1)


        return [min_r, max_r]