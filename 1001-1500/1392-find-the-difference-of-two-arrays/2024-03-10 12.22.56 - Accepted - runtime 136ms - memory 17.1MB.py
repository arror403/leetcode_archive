class Solution:
    def findDifference(self, m: List[int], n: List[int]) -> List[List[int]]:
        m=set(m)
        n=set(n)
        inter_s=m&n

        return [list(m-inter_s),list(n-inter_s)]