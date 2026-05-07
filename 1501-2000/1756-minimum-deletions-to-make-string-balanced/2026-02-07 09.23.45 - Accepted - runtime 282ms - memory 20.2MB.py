class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count=res=0

        for c in s:
            res=min(res+(c=='a'), b_count)
            b_count+=(c=='b')


        return res