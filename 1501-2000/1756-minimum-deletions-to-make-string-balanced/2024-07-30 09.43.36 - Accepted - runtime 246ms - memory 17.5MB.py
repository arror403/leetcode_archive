class Solution:
    def minimumDeletions(self, s: str) -> int:
        b_count = 0
        deletions = 0
        
        for char in s:
            if char == 'a':
                # If we've seen 'b' before, we either delete this 'a'
                # or we delete all previous 'b's
                deletions = min(deletions + 1, b_count)
            else:  # char == 'b'
                b_count += 1
        
        return deletions