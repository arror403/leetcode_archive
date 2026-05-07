class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        t=[1,2,3,4,5,6,7,8,9]
        k=itertools.combinations(t,k)
        res=[]
        for i in k:
            if sum(i)==n:
                res.append(i)

        return res