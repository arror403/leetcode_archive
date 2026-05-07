class Solution:
    def maxOperations(self, s: str) -> int:
        total_ops = 0
        ones_seen_so_far = 0

        for k, g in groupby(s):
            if k == '1':
                ones_seen_so_far += len(list(g))
            else:
                if ones_seen_so_far > 0:
                    total_ops += ones_seen_so_far


        return total_ops