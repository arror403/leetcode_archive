class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]

        for i in range(1, len(words)):
            if Counter(res[-1]) != Counter(words[i]):
                res.append(words[i])


        return res