class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        d=Counter(word)
        res=inf

        for x in d.values():
            cur=0
            for v in d.values():
                cur+=(v if v<x else max(0, v-x-k))
            
            res=min(res, cur)


        return res