class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res=0
        L=len(word)
        sub_word=[word[i:j] for i in range(L) for j in range(i+1,L+1)]
        for i in patterns:
            if i in sub_word:
                res+=1

        return res