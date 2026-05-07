class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = reduce(lambda x,y :x+y ,matrix)
        # m=[]
        # for i in matrix: m.append(i)
        return sorted(arr)[k-1]