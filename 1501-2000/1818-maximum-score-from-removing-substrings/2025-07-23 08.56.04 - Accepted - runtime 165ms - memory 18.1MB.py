class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a_count = b_count = res = 0
        lesser = min(x, y)

        for c in s:
            if c > 'b':
                res += min(a_count, b_count) * lesser
                a_count = 0
                b_count = 0
            elif c == 'a':
                if x < y and b_count > 0:
                    b_count -= 1
                    res += y
                else:
                    a_count += 1
            elif c == 'b':
                if x > y and a_count > 0:
                    a_count -= 1
                    res += x
                else:
                    b_count += 1

        res += min(a_count, b_count) * lesser
        
        return res