class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t=[]
        for j in range(0,rowIndex+1):
            t.append(self.combination(rowIndex,j))
        return(t)
        

    def combination(self, n: int, r: int) -> int:
        result=1
        p=n
        q=1
        for i in range(r):
            result=result*p
            p=p-1
            result=result/q
            q=q+1

        return int(result)