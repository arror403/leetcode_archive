class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # t=[w for i in bank if (w:=i.count('1'))>0]
        t=[]
        for i in bank:
            tmp=i.count('1')
            if tmp>0:
                t.append(tmp)

        if len(t)<=1: return 0

        return sum(t[x-1]*t[x] for x in range(1,len(t)))