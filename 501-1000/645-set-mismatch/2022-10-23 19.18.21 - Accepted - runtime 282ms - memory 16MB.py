class Solution:
    def findErrorNums(self, n: List[int]) -> List[int]:
        return [sum(n)-sum(set(n)) , sum(range(1,len(n)+1))-sum(set(n))]