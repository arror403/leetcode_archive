class Solution:
    def countCharacters(self, words: List[str], d: str) -> int:
        d=Counter(d)
        return sum([len(i) for i in words if all([c in d.keys() and f<=d[c] for c,f in Counter(i).items()])])