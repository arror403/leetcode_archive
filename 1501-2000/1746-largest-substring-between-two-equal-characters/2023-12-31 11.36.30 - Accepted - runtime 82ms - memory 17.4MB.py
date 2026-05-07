class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        if len(s)==len(set(s)): return -1
        
        d = defaultdict(list)
        for i,v in enumerate(s): d[v].append(i)
        return max([x[-1]-x[0] for x in d.values()])-1