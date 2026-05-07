class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        r=[0]*k
        for v in arr: r[v%k]+=1

        return all(r[i]==r[k-i] for i in range(1, k//2 + 1)) and r[0]%2==0