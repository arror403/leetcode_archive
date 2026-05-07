class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        s = k = 0
        d = [0] * (n + 1)
        for i in range(n):
            while (s + d[i] < nums[i]):
                if k==len(queries): return -1
                l, r = queries[k][0], queries[k][1]
                val=queries[k][2]
                k+=1
                
                if r<i: continue
                d[max(l,i)]+=val
                d[r+1]-=val
            
            s+=d[i]
        

        return k