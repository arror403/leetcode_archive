class Solution:
    def minimumCost(self,source:str,target:str,original:List[str],changed:List[str],cost:List[int])->int:
        def minimumCostFrom(sourceChar):
            bests = {}
            seenCost = defaultdict(lambda: inf)
            seenCost[sourceChar] = 0
            frontier = [(0, sourceChar)]
            while frontier:
                reachCost, current = heappop(frontier)
                if current in bests: 
                    continue
                bests[current] = reachCost
                for d, edgeCost in edges[current].items():
                    totalCost = reachCost + edgeCost
                    if totalCost < seenCost[d]:
                        heappush(frontier, (totalCost, d))
                        seenCost[d] = totalCost

            return bests


        edges = defaultdict(lambda: {})
        for i in range(len(original)):
            s, d, c = original[i], changed[i], cost[i]
            if d not in edges[s] or c < edges[s][d]:
                edges[s][d] = c

        bests = defaultdict(lambda: {})
        totalCost = 0
        for s, t in zip(source, target):
            if s != t:
                if t in bests[s]:
                    totalCost += bests[s][t]
                elif len(bests[s]) > 0:
                    return -1
                else:
                    best = minimumCostFrom(s)
                    bests[s] = best
                    if t in best:
                        totalCost += best[t]
                    else:
                        return -1


        return totalCost