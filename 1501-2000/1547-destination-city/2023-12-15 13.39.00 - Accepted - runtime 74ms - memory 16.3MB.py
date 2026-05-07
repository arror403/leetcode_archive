class Solution:
    def destCity(self, p: List[List[str]]) -> str:
        return next(x[1] for x in p if x[1] not in [i[0] for i in p])