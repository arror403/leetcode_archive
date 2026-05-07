class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = [0]*26
        print(list(tiles))
        for i in list(tiles): count[ord(i)-65]+=1
        return self.dfs(count)


    def dfs(self, arr):
        sum = 0
        for i in range(26):
            if (arr[i] == 0): continue
            sum+=1
            arr[i]-=1
            sum += self.dfs(arr)
            arr[i]+=1
        return sum