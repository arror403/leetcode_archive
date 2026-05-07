class Solution:
    def numberGame(self, n: List[int]) -> List[int]:
        n.sort()
        res=[]
        for i in range(0,len(n)-1,2):
            res.append(n[i+1])
            res.append(n[i])

        return res