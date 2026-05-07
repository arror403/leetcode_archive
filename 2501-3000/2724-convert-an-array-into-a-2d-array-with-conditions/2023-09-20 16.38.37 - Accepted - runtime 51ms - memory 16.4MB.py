class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        d=dict(collections.Counter(nums))

        d=[[k,v] for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True)]

        res=[[] for _ in range(d[0][1])]

        for i in d:
            for j in range(i[1]):
                res[j].append(i[0])

        return res