class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        n=len(arr)
        prefix=[0]*n
        prefix[0]=arr[0]
        res=0
        mp=defaultdict(int)

        for i in range(1,n): prefix[i]=arr[i]+prefix[i-1]
        
        for i in range(n):
            if prefix[i]==k: res+=1
            if (t:=prefix[i]-k) in mp: res+=mp[t]
            
            mp[prefix[i]]+=1


        return res