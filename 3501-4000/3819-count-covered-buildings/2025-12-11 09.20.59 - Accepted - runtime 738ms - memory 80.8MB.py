class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        res=0
        x=defaultdict(set)
        y=defaultdict(set)

        for a,b in buildings:
            x[a].add(b)
            y[b].add(a)

        for k,v in x.items(): x[k]=sorted(v)
        for k,v in y.items(): y[k]=sorted(v)
        
        sa=set()
        sb=set()
        for k,v in x.items():
            L=len(v)
            if L>=3:
                for i in range(1, L-1):
                    sa.add((k,v[i]))

        for k,v in y.items():
            L=len(v)
            if L>=3:
                for i in range(1, L-1):
                    sb.add((v[i],k))


        return len(sa&sb)