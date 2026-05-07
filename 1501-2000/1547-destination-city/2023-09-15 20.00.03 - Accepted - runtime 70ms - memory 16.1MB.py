class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list({i[1] for i in paths}-{i[0] for i in paths})[0]