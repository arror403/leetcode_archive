class Solution:
    def similarPairs(self, words: List[str]) -> int:
        return sum([v*(v-1)//2 for v in Counter([''.join(sorted(set(i))) for i in words]).values()])