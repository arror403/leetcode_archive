class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d=defaultdict(int)
        for k,v in (items1+items2): d[k]+=v

        return sorted([[k,v] for k,v in d.items()],key=lambda x:x[0])