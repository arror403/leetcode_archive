class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows, cols = len(M), len(M[0])
        result = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                result[i][j] = self.get_smoothed_value(M, i, j, rows, cols)

        return result

    def get_smoothed_value(self, M, i, j, rows, cols):
        total_sum, count = 0, 0

        for x in range(max(0, i - 1), min(rows, i + 2)):
            for y in range(max(0, j - 1), min(cols, j + 2)):
                total_sum += M[x][y]
                count += 1

        return total_sum // count

        # m,n=len(img),len(img[0])
        # if (m<3 or n<3): return img


        # for i in range(1,m-1):
        #     for j in range(1,n-1):
        #         a=(img[i-1][j-1]+img[i-1][j+1]+img[i+1][j-1]+img[i+1][j+1])
        #         b=(img[i+1][j]+img[i][j+1]+img[i-1][j]+img[i][j-1])
        #         img[i-1][j-1]=img[i-1][j+1]=img[i+1][j-1]=img[i+1][j+1]=floor(a/4)
        #         img[i+1][j]=img[i][j+1]=img[i-1][j]=img[i][j-1]=floor(b/4)
        #         img[i][j]=floor((a+b+img[i][j])/9)

        # return img