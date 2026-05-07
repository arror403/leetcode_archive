class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr=[i for i in arr if arr.count(i)==1]
        
        # print(arr)
        
        return arr[k-1] if k<=len(arr) else ''