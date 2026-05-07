class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        L = len(isConnected)

        def dfs(isConnected, visited, i):
            for j in range(L):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(isConnected, visited, j)


        visited = [0]*L
        res = 0
        for i in range(L):
            if visited[i] == 0:
                dfs(isConnected, visited, i)
                res += 1


        return res