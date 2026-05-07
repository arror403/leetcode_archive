class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        counts = [w.count('1') for w in bank if '1' in w]
        return sum(counts[i-1]*counts[i] for i in range(1, len(counts))) if len(counts)>1 else 0