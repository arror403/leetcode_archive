class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = reduce(lambda x,y :x+y ,matrix)
        return sorted(arr)[k-1]