class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        mod=10**9+7
        dp_zero=[0]*n
        dp_one=[0]*n
        res=0
        arr=[v%2 for v in arr]

        if arr[n-1]:
            dp_one[n-1]=1
        else:
            dp_zero[n-1]=1
        
        for i in range(n-2,-1,-1):
            if arr[i]==1:
                dp_one[i]=(1+dp_zero[i+1])%mod
                dp_zero[i]=dp_one[i+1]
            
            if arr[i]==0:
                dp_zero[i]=(1+dp_zero[i+1])%mod
                dp_one[i]=dp_one[i+1]
   
        

        for v in dp_one:
            res+=v 
            res%=mod
        

        return res