class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count=deletions=0

        for c in s:
            deletions=min(deletions+(c=='a'), b_count)
            b_count+=(c=='b')


        return deletions