class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        L = len(groups)
        if L == 1: return words
        

        for start in range(L):
            curr = [words[start]]
            last_group = groups[start]
            
            for i in range(start + 1, L):
                if groups[i] != last_group:
                    curr.append(words[i])
                    last_group = groups[i]
            
            res.append(curr)
            
        return max(res, default=[], key=len)