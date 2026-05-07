class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return int('1'*len(bin(n)[2:]), 2) ^ n
        
        # return [1,0][n] if n<2 else n ^ ((1 << int(log2(n)+1)) - 1)