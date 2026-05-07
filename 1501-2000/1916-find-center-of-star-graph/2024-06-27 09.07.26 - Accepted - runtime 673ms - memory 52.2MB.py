class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        # return Counter(chain.from_iterable(edges)).most_common(len(edges)-1)
        return list(reduce(lambda a,b: a&b, map(set, edges)))[0]