class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(x, y): return ((x&1)<<1)|(y&1)

        n=len(s)
        res=-inf

        for a in "01234":
            for b in "01234":
                if a==b: continue

                best=[inf]*4
                cnt_a = cnt_b = prev_a = prev_b = 0
                left=-1

                for right in range(n):
                    cnt_a += 1 if s[right]==a else 0
                    cnt_b += 1 if s[right]==b else 0

                    while (right-left>=k) and (cnt_b-prev_b>=2):
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left+=1
                        prev_a += 1 if s[left]==a else 0
                        prev_b += 1 if s[left]==b else 0

                    right_status = getStatus(cnt_a, cnt_b)
                    required_status = right_status ^ 2
                    if best[required_status]!=inf:
                        res = max(res, cnt_a - cnt_b - best[required_status])


        return res