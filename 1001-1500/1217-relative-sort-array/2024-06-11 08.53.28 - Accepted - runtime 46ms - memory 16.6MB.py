class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p={k:i for i,k in enumerate(arr2)}
        good,bad=[],[]
        for x in arr1: good.append(x) if x in arr2 else bad.append(x) 

        return sorted(good, key=lambda x:p.get(x))+sorted(bad)