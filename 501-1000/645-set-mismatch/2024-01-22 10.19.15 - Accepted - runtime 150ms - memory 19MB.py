class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        s=set(n)
        t=set(range(1,len(n)+1))
        return [sum(n)-sum(s) , (t-s).pop()]