class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # t = [set(x) for x in arr]
        res=0

        for i in range(len(arr),0,-1):
            for c in combinations(arr,i):
                # print(''.join(t))
                t=''.join(c)
                l=len(t)
                if len(set(t))==l:
                    res=max(res,l)
                    
        return res