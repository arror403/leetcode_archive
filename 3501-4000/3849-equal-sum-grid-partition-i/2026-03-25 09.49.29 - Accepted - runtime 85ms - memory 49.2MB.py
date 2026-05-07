class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        r_sum=list(accumulate([sum(r) for r in grid]))
        S=r_sum[-1]
        # print(r_sum)
        for i in range(m-1):
            if (S-r_sum[i])==r_sum[i]:
                # print(r_sum[i])
                return True

        c_sum=list(accumulate([sum(c) for c in zip(*grid)]))
        # print(c_sum)
        for i in range(n-1):
            if (S-c_sum[i])==c_sum[i]:
                # print(c_sum[i])
                return True
        

        return False