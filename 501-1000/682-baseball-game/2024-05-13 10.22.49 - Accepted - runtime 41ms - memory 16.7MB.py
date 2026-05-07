class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res=[]

        for p in operations:
            # print(res)
            if p not in ["C", "D", "+"]:
                res.append(int(p))
            elif p=='+':
                res.append(res[-1]+res[-2])
            elif p=='D':
                res.append(res[-1]*2)
            elif p=='C':
                res.pop()

        
        return sum(res)