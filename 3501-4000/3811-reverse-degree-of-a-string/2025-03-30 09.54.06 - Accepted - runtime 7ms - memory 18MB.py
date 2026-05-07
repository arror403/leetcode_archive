class Solution:
    def reverseDegree(self, s: str) -> int:
        d={chr(i):(123-i) for i in range(97,123)}
        return sum((i+1)*d[c] for i,c in enumerate(s))