class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        return all((x==(0,1) or x==(1,0)) for x in pairwise(map(lambda x:x%2, nums)))