class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        res=[]
        for i in range(len(capacity)):
            if capacity[i]>=itemSize:
                res.append([i,capacity[i]])

        return sorted(res, key=lambda x:(x[1],x[0]))[0][0] if res else -1