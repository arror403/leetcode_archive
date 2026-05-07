class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)
        res=[[] for _ in range(d[0][1])]

        for v,f in d:
            for j in range(f):
                res[j].append(v)

        return res