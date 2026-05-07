class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        A.sort()
        for i in range(0,len(A)-1):
            if A[i]==A[i+1]:
                b=A[i]
                break
            
        return b