class Solution:
    def luckyNumbers (self, m: List[List[int]]) -> List[int]:
        # a={min(r) for r in m}

        # b={min(map(lambda x: x[i], m)) for i in range(len(m[0]))}
            

        # return list(a&b)

        return [min(r) for r in m for i in range(len(m[0])) if max(map(lambda x:x[i],m))==min(r)]