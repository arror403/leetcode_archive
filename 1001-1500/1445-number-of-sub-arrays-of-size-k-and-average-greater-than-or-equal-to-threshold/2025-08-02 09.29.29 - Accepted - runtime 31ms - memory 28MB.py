class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        s, t, res = sum(arr[:k]), k*threshold, 0
        # print(s,t)
        if s>=t: res+=1

        for i in range(k, len(arr)):
            s-=arr[i-k]
            s+=arr[i]
            # print(s)
            if s>=t: res+=1

        
        return res