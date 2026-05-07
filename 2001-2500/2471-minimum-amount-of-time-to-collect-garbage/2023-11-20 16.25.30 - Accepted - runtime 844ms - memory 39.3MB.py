class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        res = len(''.join(garbage))

        # d=defaultdict(int)
        d={}

        for i,house in enumerate(garbage):
            for g in house:
                d[g] = i

        presum = [0]

        for t in travel: 
            presum.append(presum[-1] + t)

        for k,v in d.items(): 
            res += presum[v]

        return res



        # res = 0
        # t = Counter(''.join(garbage))
        # res += sum(t.values())

        # for garbage_type in ['G', 'P', 'M']:
        #     if t[garbage_type] > 0:
        #         for i in range(len(travel)):
        #             if garbage_type in garbage[i+1]:
        #                 res += travel[i]

        # return res



        
        # res=0
        # t=Counter(''.join(garbage))
        # res+=sum(t.values())
        # d=len(travel)

        # if t['G']>0:
        #     x=0
        #     while x<d:
        #         if 'G' in garbage[x+1]: res+=travel[x]
        #         x+=1


        # if t['P']>0:
        #     x=0
        #     while x<d:
        #         if 'P' in garbage[x+1]: res+=travel[x]
        #         x+=1


        # if t['M']>0:
        #     x=0
        #     while x<d:
        #         if 'M' in garbage[x+1]: res+=travel[x]
        #         x+=1


        # return res