class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return Counter(chain.from_iterable(edges)).most_common(1)[0][0]