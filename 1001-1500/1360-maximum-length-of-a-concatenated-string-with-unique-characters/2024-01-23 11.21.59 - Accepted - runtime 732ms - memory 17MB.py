class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res = []

        for i in range(1, len(arr) + 1):
            for x in combinations(arr, i):
                w = ''.join(x)
                if len(w) == len(set(w)):
                    res.append(len(w))

        return max(res, default=0)