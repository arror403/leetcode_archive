class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        f=Counter(arr).values()
        d=set(f)
        return len(d)==len(f)