class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return sum(list(filter(lambda t: t%3==0 or t%5==0 or t%7==0, [x for x in range(1,n+1)])))