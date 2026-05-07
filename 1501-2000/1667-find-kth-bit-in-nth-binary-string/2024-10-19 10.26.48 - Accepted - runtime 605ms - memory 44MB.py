class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s=["0"]
        for _ in range(n): s+=(["1"]+["0" if c=="1" else "1" for c in s][::-1])

        return s[k-1]