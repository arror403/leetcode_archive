class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p={k:i for i,k in enumerate(arr2)}
        #useful method; found on stackoverflow
        a,b=[],[]
        for x in arr1: (b,a)[x in arr2].append(x)

        return sorted(a, key=lambda x:p[x])+sorted(b)