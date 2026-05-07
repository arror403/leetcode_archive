class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        r, c = len(isWater), len(isWater[0])
        curr = deque()
        hill = 0
        
        for i in range(r):
            for j in range(c):
                # set the land cell to -1 (not visited)
                if (isWater[i][j] == 0):
                    isWater[i][j] = -1
                # set the water cell to zero and to queue
                else:
                    isWater[i][j] = 0
                    curr.append([i, j])
        
        while curr:
            for _ in range(len(curr)):           
                # for each cell check its 4 boundary cells
                # if it is not visited, increase its hill by 1
                i, j = curr.popleft()
                # top
                if (i > 0 and isWater[i - 1][j] == -1):
                    isWater[i - 1][j] = hill + 1
                    curr.append([i-1, j])
                # bottom
                if ((i < r - 1) and (isWater[i + 1][j] == -1)):
                    isWater[i + 1][j] = hill + 1
                    curr.append([i+1, j])
                # left
                if (j > 0 and (isWater[i][j - 1] == -1)):
                    isWater[i][j - 1] = hill + 1
                    curr.append([i, j-1])
                # right
                if ((j < c - 1) and (isWater[i][j + 1] == -1)):
                    isWater[i][j + 1] = hill + 1
                    curr.append([i, j+1])
            
            # after 1 complete round increase the height of the hill
            hill += 1


        return isWater