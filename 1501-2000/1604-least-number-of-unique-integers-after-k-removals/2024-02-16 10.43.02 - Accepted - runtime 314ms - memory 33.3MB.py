class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        ##### improved by chatGPT #####

        d=sorted(Counter(arr).values())
        res=len(d)

        for f in d:
            if f<=k:
                k-=f
                res-=1
            else:
                break

        return res