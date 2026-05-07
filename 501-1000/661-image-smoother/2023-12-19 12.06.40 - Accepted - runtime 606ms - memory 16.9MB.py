class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def neighbors(row_number, column_number):
            return (
                img[i][j] if 0 <= i < m and 0 <= j < n else -1
                for i in range(row_number - 1, row_number + 2)
                for j in range(column_number - 1, column_number + 2)
            )

        res = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                t = [x for x in neighbors(i, j) if x != -1]
                res[i][j] = floor(sum(t) / len(t))

        return res