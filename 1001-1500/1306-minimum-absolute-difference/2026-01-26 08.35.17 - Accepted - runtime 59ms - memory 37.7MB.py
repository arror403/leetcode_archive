class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        p=list(pairwise(arr))
        m=min([b-a for a,b in p])
        
        return [[a,b] for a,b in p if (b-a)==m]