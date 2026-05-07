class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        count = 0
        for i in range(1,len(A)):
            if (A[i] == A[i-1]):
                count+=1
            else:
                A[i-count] = A[i]
        return len(A)-count