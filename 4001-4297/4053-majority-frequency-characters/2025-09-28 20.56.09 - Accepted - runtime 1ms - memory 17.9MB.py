class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = defaultdict(set)

        for v, f in Counter(s).items(): d[f].add(v)

        d = sorted(d.items(), key=lambda x: (len(x[1]), x[0]))
        
        # print(d)
        return ''.join(list(d[-1][1]))