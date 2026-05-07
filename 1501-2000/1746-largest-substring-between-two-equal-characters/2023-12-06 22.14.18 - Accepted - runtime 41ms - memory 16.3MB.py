class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        # d={}
        # for i,v in enumerate(s):
        #     if v not in d:
        #         d[v]=[i]
        #     else:
        #         d[v].append(i)

        d = defaultdict(list)
        for i,v in enumerate(s): d[v].append(i)
        return max([x[-1]-x[0] for x in d.values()])-1