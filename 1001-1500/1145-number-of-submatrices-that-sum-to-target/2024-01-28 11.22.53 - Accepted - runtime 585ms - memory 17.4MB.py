class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:

        ##### power by COPILOT #####

        m, n = len(matrix), len(matrix[0])
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]
        count = 0
        for r1 in range(1, m + 1):
            for r2 in range(r1, m + 1):
                h = defaultdict(int)
                h[0] = 1
                for c in range(1, n + 1):
                    curr_sum = prefix[r2][c] - prefix[r1 - 1][c]
                    count += h[curr_sum - target]
                    h[curr_sum] += 1
        return count