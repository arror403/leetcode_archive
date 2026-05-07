class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        return [len(set(A[:i]) & set(B[:i])) for i in range(1,len(A)+1)]
            