class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        t=int(len(arr)*0.05)
        arr=arr[t:]
        arr=arr[:-t]

        return sum(arr)/len(arr)