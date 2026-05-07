class Solution:
    def maxLength(self, arr: List[str]) -> int:
        L=len(arr)
        t=chain.from_iterable([[w for x in (combinations(arr,i)) if len(w:=''.join(map(str,x)))==len(set(w))] for i in range(1,L+1)])
        res=max(t,key=len,default='')

        return len(res)