class Solution:
    def replaceElements(self, arr: List[int], m=-1) -> List[int]:
        for i in range(len(arr)-1,-1,-1): arr[i], m = m, max(m, arr[i])

        return arr