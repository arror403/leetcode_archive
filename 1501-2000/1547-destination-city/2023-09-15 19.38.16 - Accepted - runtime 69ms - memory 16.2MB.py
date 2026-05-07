class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list({j for i in paths for j in i}-{i[0] for i in paths})[0]