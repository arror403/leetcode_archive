class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        m = list(permutations(range(1, n+1)))
        
        return ''.join([str(x) for x in m[k-1]])