class Solution:
    def maxLength(self, A: List[str]) -> int:
        t=chain.from_iterable([[w for x in (combinations(A,i)) if len(w:=''.join(map(str,x)))==len(set(w))] for i in range(1,len(A)+1)])

        return len(max(t,key=len,default=''))