class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_so_far = -1
        return [(max_so_far := max(max_so_far, arr[i+1])) for i in range(len(arr)-2, -1, -1)][::-1] + [-1]