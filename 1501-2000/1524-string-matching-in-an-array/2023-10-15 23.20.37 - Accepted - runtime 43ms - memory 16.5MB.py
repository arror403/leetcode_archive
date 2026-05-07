class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # print(list(combinations(sorted(words,key=lambda x:len(x)),2)))
        return list(set([i for i,j in list(combinations(sorted(words,key=lambda x:len(x)),2)) if i in j]))