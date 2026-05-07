class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        l=len(arr)
        arr[0]=1

        for i in range(l-1):
            if (arr[i+1]-arr[i])>=1:
                arr[i+1]=arr[i]+1

        # print(arr)

        return arr[-1]