class Solution:
    def countTestedDevices(self, b: List[int]) -> int:
        L=len(b)
        res=i=0
        while i<L:
            if b[i]>0:
                res+=1
                for j in range(i+1,L): b[j]=max(0,b[j]-1)
            i+=1

        return res