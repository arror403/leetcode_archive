class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # return Counter(chain.from_iterable(edges)).most_common(len(edges)-1)
        return list(set(edges[0])&set(edges[1]))[0]