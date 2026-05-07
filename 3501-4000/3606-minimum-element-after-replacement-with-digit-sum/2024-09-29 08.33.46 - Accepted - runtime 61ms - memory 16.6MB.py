class Solution:
    def minElement(self, nums: List[int]) -> int:
        return min(map(lambda x:sum(map(int,str(x))), nums))