class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        t=sorted(Counter(chain.from_iterable(roads)).values(), reverse=1)
        return sum(t[i]*(n-i) for i in range(len(t)))