class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums=[]
        for i in range(1,n+1): nums.append(i)
        m=list(itertools.permutations(nums))
        
        res=''.join([str(x) for x in m[k-1]])
        
        return res