class Solution:
    def binaryGap(self, n: int) -> int:
        ind=[i for i,c in enumerate(bin(n)[2:]) if c=='1']

        return max((b-a for a,b in pairwise(ind)), default=0)