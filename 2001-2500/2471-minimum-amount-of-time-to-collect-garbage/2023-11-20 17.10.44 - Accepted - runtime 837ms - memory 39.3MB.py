class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:

        d = {g:i for i,house in enumerate(garbage) for g in house}
        
        return sum([list(accumulate([0]+travel))[v] for v in d.values()])+len(''.join(garbage))
        
        
        # res = 0
        # t = Counter(''.join(garbage))
        # res += sum(t.values())

        # for garbage_type in ['G', 'P', 'M']:
        #     if t[garbage_type] > 0:
        #         for i in range(len(travel)):
        #             if garbage_type in garbage[i+1]:
        #                 res += travel[i]

        # return res