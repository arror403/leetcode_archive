class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        r=Counter(arr).values()
        return len(r)==len(set(r))