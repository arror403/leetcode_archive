class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        
        total_cost = 0
        n = len(costs) // 2
        
        # Send first n people to city A
        for i in range(n):
            total_cost += costs[i][0]
        
        # Send last n people to city B
        for i in range(n, 2*n):
            total_cost += costs[i][1]
        
        return total_cost


        
        # l,r=[],[]
        # res=0
        # L=len(costs)

        # for a,b in costs:
        #     l.append(a)
        #     r.append(b)

        # l.sort()
        # r.sort()

        # i=j=0
        # for _ in range(L):
        #     if l[i]<r[j]:
        #         res+=l[i]
        #         i+=1
        #     else:
        #         res+=r[j]
        #         j+=1