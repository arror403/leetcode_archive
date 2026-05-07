class Solution:
    def subarraysDivByK(self, arr: List[int], k: int) -> int:
        mod=[0]*(k+1)
        cumSum=list(accumulate(arr))
        for i in range(len(arr)): mod[(cumSum[i]%k+k)%k]+=1
        return sum((mod[i]*(mod[i]-1))//2 for i in range(k) if (mod[i]>1))+mod[0]