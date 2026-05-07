class Solution:
    def subarraysDivByK(self, arr: List[int], k: int) -> int:
        mod=[0]*(k+1)
        cumSum=0
        res=0

        for i in range(len(arr)):
            cumSum+=arr[i]
            mod[((cumSum%k)+k)%k]+=1
        
        for i in range(k):
            if (mod[i]>1):
                res+=(mod[i]*(mod[i]-1))//2

        res+=mod[0]
        

        return res