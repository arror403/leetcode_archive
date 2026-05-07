class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            f = Counter(s)
            res.setdefault(tuple(sorted(f.items())), []).append(s)

        return list(res.values())