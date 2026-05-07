class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        L=len(grid)
        s=[]
        for r in grid:
            z=0
            for i in range(L-1,-1,-1):
                if r[i]==0:
                    z+=1
                else:
                    break
            s.append(z)
                
        swaps=0
        for i in range(L):
            needed = L-i-1
            j=i
            while j<L and s[j]<needed:
                j+=1
            if j==L:
                return -1
            while j>i:
                s[j], s[j - 1] = s[j - 1], s[j]
                j-=1
                swaps+=1

        return swaps