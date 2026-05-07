class Solution:
    def prefixConnected(self, words: List[str], k: int) -> int:
        d=defaultdict(int)

        for w in words:
            if len(w)<k: continue
            d[w[:k]]+=1


        return len([v for v in d.values() if v>1])