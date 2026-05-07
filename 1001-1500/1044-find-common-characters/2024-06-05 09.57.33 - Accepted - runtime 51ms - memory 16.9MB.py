class Solution:
    ##### improved by chatGPT #####
    def commonChars(self, words: List[str]) -> List[str]:
        d = list(map(Counter, words))
        res = []
        
        for char, count in reduce(lambda x,y:x&y, d).items():
            res.extend([char] * count)
        
        return res