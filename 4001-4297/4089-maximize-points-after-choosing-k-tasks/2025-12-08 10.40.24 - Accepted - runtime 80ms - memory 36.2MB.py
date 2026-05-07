class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        m = sorted([b-a if b>a else 0 for a,b in zip(technique1, technique2)], reverse=True)

        return sum(technique1) + sum(m[:len(technique1)-k])