class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d=sorted([[v,f] for v,f in Counter(s).items()], key=lambda x:x[1])
        L,res=len(d),0
        d=deque(d)

        while L>k:
            _,c=d.popleft()
            L-=1
            res+=c


        return res