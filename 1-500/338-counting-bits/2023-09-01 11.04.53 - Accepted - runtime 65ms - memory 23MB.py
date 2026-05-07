class Solution:
    def countBits(self, num: int) -> List[int]:
        b = [0] * (num + 1)
        
        for i in range(1, num + 1):
            # Using Brian Kernighan's algorithm to count set bits
            b[i] = b[i & (i - 1)] + 1
        
        return b