class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        d = Counter(arr)
        res = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                a, b = arr[i], arr[j]
                l = 2
                while d[a+b]:
                    b = a + b
                    a = b - a
                    l += 1

                res = max(res, l)


        return res if res > 2 else 0