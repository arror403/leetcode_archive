class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        min_c = {}
        max_c = {}
        min_r = {}
        max_r = {}

        for a,b in buildings:
            if a not in min_c:
                min_c[a] = b
                max_c[a] = b
            else:
                if b < min_c[a]: min_c[a] = b
                elif b > max_c[a]: max_c[a] = b
            
            if b not in min_r:
                min_r[b] = a
                max_r[b] = a
            else:
                if a < min_r[b]: min_r[b] = a
                elif a > max_r[b]: max_r[b] = a

        res = 0
        for a,b in buildings:
            if min_c[a] < b < max_c[a]:
                if min_r[b] < a < max_r[b]:
                    res += 1
                    

        return res