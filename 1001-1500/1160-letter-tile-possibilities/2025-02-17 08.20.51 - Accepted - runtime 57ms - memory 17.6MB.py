class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count=[0]*26
        for c in tiles: count[ord(c)-65]+=1

        def dfs(arr):
            res=0
            for i in range(26):
                if arr[i]==0: continue
                res+=1
                arr[i]-=1
                res+=dfs(arr)
                arr[i]+=1

            return res


        return dfs(count)