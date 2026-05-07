class Solution:
    def reorderedPowerOf2(self, x: int) -> bool:
        d=Counter(str(x))
        # d=defaultdict(int)
        
        
        m=[]
        n=1
        while n<=10**9:
            # d.clear()
            # for c in str(n): d[c]+=1
            # m.append(d)
            m.append(Counter(str(n)))
            n*=2

        # d.clear()
        # for c in str(x): d[c]+=1

        # print(m)
        return d in m