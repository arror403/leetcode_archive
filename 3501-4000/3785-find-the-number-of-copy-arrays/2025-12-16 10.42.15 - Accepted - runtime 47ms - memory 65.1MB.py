class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        l, h = bounds[0][0], bounds[0][1]

        for i in range(1, len(original)):
            d = original[i] - original[i-1]
            l += d
            h += d
            l = max(l, bounds[i][0])
            h = min(h, bounds[i][1])

            if h < l: return 0

        # print(l,h)
        return h-l+1