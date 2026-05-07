class Solution:
    def toHex(self, num: int) -> str:
        if num >=0:
            return hex(num)[2:]
        else:
            return self.tohex(num, 32)[2:]

    def tohex(self, val, nbits):
        return hex((val + (1 << nbits)) % (1 << nbits))