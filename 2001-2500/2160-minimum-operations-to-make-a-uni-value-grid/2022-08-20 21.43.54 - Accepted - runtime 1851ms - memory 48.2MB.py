class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # m=reduce(lambda x,y: x+y, grid)
        m = sorted([c for r in grid for c in r])
        res=0
        tmp=m[len(m)//2]
        # if len(m)%2==1:
        #     tmp=m[len(m)//2]
        # else:
        #     tmp=m[len(m)//2-1]
        del m
        
        for r in grid:
            for c in r:
                if (tmp-c)%x != 0: return -1
                
                if tmp>c: res+=(tmp-c)/x
                elif tmp==c: continue
                else: res+=(c-tmp)/x
            
        return int(res)