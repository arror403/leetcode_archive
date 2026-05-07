class Solution:
    def numOfStrings(self, p: List[str], w: str) -> int:
        return sum(1 for i in p if i in [w[i:j] for i in range(len(w)) for j in range(i+1,len(w)+1)])