class Solution:
    def minTimeToType(self, word: str) -> int:
        res=len(word)
        pre="a"
        for i in word:
            tmp=(ord(i)-ord(pre))%26
            res+=min(tmp,26-tmp)
            pre=i

        return res