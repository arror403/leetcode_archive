class Solution:
    def minimumSum(self, num: int) -> int:
        num=list(map(int,str(num)))
        m=list(itertools.permutations(num))
        m=[list(i) for i in m]
        # print(m)
        res=inf
        for i in m:
            tmp=[str(x) for x in i]
            tmp=''.join(tmp)
            tmp=int(tmp[:2])+int(tmp[2:])
            if tmp<res:
                res=tmp
                
        for i in m:
            tmp=[str(x) for x in i]
            tmp=''.join(tmp)
            tmp=int(tmp[:1])+int(tmp[1:])
            if tmp<res:
                res=tmp
                
        for i in m:
            tmp=[str(x) for x in i]
            tmp=''.join(tmp)
            tmp=int(tmp[:3])+int(tmp[3:])
            if tmp<res:
                res=tmp
        
        return res