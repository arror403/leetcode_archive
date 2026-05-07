class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            f = tuple(sorted(Counter(s).items()))
            
            if f in res:
                res[f].append(s)
            else:
                res[f] = [s]

        return list(res.values())