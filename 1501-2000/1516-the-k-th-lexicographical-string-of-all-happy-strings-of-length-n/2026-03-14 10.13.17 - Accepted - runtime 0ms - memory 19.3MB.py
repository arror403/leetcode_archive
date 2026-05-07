class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3*(1<<(n-1)): return ""
        res = []
        pre = ""
        
        for i in range(n):
            # Try characters in lexicographical order
            for c in ['a', 'b', 'c']:
                # Adjacent chars cannot be the same
                if c == pre:
                    continue
                # Number of strings if we choose this character here
                remaining_len = n - i - 1
                cnt = 1 << remaining_len   # 2^remaining_len
                if k > cnt:
                    # Skip this whole block
                    k -= cnt
                else:
                    # This character belongs to the kth string
                    res.append(c)
                    pre = c
                    break


        return "".join(res)