class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d=sorted(Counter(arr).items(), key=lambda x:x[1])
        res=len(d)
        for _,f in d:
            if f<=k:
                k-=f
                res-=1
            else:
                break
        return res