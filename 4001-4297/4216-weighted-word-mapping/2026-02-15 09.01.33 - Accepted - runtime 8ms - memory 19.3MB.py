class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        return ''.join([chr(122-sum(weights[ord(s)-97] for s in w)%26) for w in words])