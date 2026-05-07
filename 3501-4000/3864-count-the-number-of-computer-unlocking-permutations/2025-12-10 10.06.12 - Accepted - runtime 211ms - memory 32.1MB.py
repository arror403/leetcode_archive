class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        m=min(complexity)
        if complexity.count(m)>1 or complexity[0]!=m: return 0

        return factorial(len(complexity)-1) % (10**9+7)