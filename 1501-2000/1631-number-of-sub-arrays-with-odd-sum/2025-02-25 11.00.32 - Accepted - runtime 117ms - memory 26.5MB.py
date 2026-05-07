class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        dp_zero=[0]*n
        dp_one=[0]*n
        arr=[v%2 for v in arr]

        if arr[n-1]:
            dp_one[n-1]=1
        else:
            dp_zero[n-1]=1
        
        for i in range(n-2,-1,-1):
            if arr[i]:
                dp_one[i] = 1 + dp_zero[i+1]
                dp_zero[i] = dp_one[i+1]
            else:
                dp_zero[i] = 1 + dp_zero[i+1]
                dp_one[i] = dp_one[i+1]


        return sum(dp_one)%(10**9+7)