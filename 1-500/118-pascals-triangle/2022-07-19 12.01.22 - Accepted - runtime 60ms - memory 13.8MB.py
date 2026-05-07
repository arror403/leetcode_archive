class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output=[]
        for i in range(0,numRows):
            t=[]
            for j in range(0,i+1):
                t.append(self.combination(i,j))
            output.append(t)
        return(output)
        
        
        
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