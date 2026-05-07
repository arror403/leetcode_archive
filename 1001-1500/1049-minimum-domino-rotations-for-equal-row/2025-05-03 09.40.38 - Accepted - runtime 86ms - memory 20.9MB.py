class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        pt=Counter(tops).most_common()[0][0]
        pb=Counter(bottoms).most_common()[0][0]
        tile=list(zip(tops, bottoms))
        ra=rb=0

        for a,b in tile:
            if a==pt:
                continue
            elif b==pt:
                ra+=1
            else: 
                ra=inf
                break

        for a,b in tile:
            if b==pb: 
                continue
            elif a==pb:
                rb+=1 
            else: 
                rb=inf
                break


        return -1 if ra==inf and rb==inf else min(ra, rb)