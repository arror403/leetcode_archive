class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        row_sum=[]
        # Matrix=[[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
        for i in range(0,len(accounts)):
            sum=0
            for j in range(0,len(accounts[0])):
                sum+=(accounts[i][j])
            row_sum.append(sum)
            row_sum.sort()

        # print(Matrix)
        return (row_sum[-1])