class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # output=[]
        # for i in range(numRows):
        #     t=[]
        #     for j in range(i+1):
        #         t.append(math.comb(i,j))
        #     output.append(t)
        # return output
        
        return [[math.comb(i,j) for j in range(i+1)] for i in range(numRows)]