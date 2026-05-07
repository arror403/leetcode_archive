class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [i[0] for i in sorted(Counter(sorted(words)).items(), key=lambda x:x[1], reverse=True)][:k]