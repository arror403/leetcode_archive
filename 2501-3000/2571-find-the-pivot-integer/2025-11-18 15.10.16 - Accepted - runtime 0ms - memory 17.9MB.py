class Solution:
    def pivotInteger(self, n: int) -> int:
        d={1:1, 8:6, 49:35, 288:204}

        return d[n] if n in d.keys() else -1