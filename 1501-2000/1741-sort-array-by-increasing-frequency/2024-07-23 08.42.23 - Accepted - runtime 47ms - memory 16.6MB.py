class Solution:
    def frequencySort(self, m: List[int]) -> List[int]:
        return chain.from_iterable([k]*f for k,f in sorted(Counter(m).items(), key=lambda x:(x[1],-x[0])))