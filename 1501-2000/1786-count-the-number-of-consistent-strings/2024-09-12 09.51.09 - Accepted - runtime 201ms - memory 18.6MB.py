class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=len(words)
        alpha={chr(97+i):False for i in range(26)}

        for c in allowed: alpha[c]=True

        for word in words:
            for c in word:
                if not alpha[c]:
                    res-=1
                    break


        return res