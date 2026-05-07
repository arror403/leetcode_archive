class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # t=[]
        # for j in range(0,rowIndex+1):
        #     t.append(self.combination(rowIndex,j))
        # return(t)

        return [math.comb(rowIndex,j) for j in range(rowIndex+1)]