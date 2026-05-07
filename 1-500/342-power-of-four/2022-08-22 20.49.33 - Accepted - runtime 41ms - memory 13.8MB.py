class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        b=[1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]
        return 1 if n in b else 0