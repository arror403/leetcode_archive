class Solution:
    def luckyNumbers (self, m: List[List[int]]) -> List[int]:
        # a={min(r) for r in m}

        # b={min(map(lambda x: x[i], m)) for i in range(len(m[0]))}
            

        # return list(a&b)

        return list({min(r) for r in m}&{max(c) for c in zip(*m)})