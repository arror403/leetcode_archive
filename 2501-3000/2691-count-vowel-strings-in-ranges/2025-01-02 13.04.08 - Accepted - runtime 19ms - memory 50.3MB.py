class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        V=set("aeiou")
        p=[0]+list(accumulate([int(((w[0] in V) and (w[-1] in V))) for w in words]))

        return [p[r+1]-p[l] for l,r in queries]