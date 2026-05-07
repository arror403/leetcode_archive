class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for w in words:
            tmp=0
            for s in w:
                tmp+=weights[ord(s)-97]
    
            res+=chr(26 - tmp%26 + 96)

        return res