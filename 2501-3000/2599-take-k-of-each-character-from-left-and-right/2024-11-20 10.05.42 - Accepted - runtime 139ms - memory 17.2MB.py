class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        limits={c:s.count(c)-k for c in 'abc'}

        if any(x < 0 for x in limits.values()): return -1

        d={c:0 for c in 'abc'}
        res=l=0

        for i,c in enumerate(s):
            d[c]+=1

            while d[c]>limits[c]:
                d[s[l]]-=1
                l+=1

            res=max(res, i-l+1)


        return len(s)-res