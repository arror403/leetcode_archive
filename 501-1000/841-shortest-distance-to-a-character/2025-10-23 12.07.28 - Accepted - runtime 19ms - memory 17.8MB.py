class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ind = [i for i, v in enumerate(s) if v == c]
        
        res = []
        for i, v in enumerate(s):
            if i in ind: 
                res.append(0)
            else:
                res.append(min([abs(i-x) for x in ind]))


        return res