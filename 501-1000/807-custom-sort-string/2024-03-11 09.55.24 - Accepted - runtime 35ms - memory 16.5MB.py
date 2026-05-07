class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res=[]
        d=defaultdict(int)

        for i,v in enumerate(order): d[v]=i    
        
        for k in s: res.append([k,d[k]])

        return ''.join([i[0] for i in sorted(res, key=lambda x:x[1])])