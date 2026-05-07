class Solution:
    def findDifference(self, m: List[int], n: List[int]) -> List[List[int]]:
        m=set(m)
        n=set(n)

        return [list(m-n),list(n-m)]