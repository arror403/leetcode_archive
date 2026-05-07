class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        proc = []
        res = m = 0  # m : max value of finished event so far

        for s,e,v in events:
            proc.append((s, True, v))       # time, is_start, val
            proc.append((e+1, False, v))    # use e+1 (inclusive)

        proc.sort()
        
        for time, is_start, val in proc:
            if is_start:
                res = max(res, m+val)
            else:
                m = max(m, val)


        return res
