class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        arr2XorSum = reduce(lambda a,b: a^b, arr2)
        
        arr1XorSum = reduce(lambda a,b: a^b, arr1)
        
        return arr1XorSum & arr2XorSum