class Solution:
    def splitNum(self, num: int) -> int:
        t=sorted(list(str(num)))

        return int(''.join(t[::2]))+int(''.join(t[1::2]))