class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        amt = {a:b for a,b in fruits}
        
        # Every position with fruit except the start position.
        position = [x[0] for x in fruits if x[0] != startPos]
        lft, rgt, n = [], [], len(position)
        idx = bisect_right(position, startPos)

        # Right pre-sum
        cur_f = 0
        for i in range(idx, n):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            rgt.append([cur_pos - startPos, cur_f])
        
        # Left pre-sum
        cur_f = 0
        for i in range(idx - 1, -1, -1):
            cur_pos = position[i]
            cur_f += amt[cur_pos]
            lft.append([startPos - cur_pos, cur_f])
        
        # Go right then turn left
        ans = 0
        for r_dist, r_f in rgt:
            if r_dist <= k:
                cur_f = r_f
                l_dist = k - 2 * r_dist
                if l_dist > 0:             # Check fruit collected from the left side.
                    idx = bisect_right(lft, [l_dist, float('inf')])
                    if idx > 0:
                        cur_f += lft[idx - 1][1]
                ans = max(ans, cur_f)
        
        # Go left then turn right
        for l_dist, l_f in lft:
            if l_dist <= k:
                cur_f = l_f
                r_dist = k - 2 * l_dist
                if r_dist > 0:             # Check fruit collected from the right side.
                    idx = bisect_right(rgt, [r_dist, float('inf')])
                    if idx > 0:
                        cur_f += rgt[idx - 1][1]
                ans = max(ans, cur_f)


        return ans + amt.get(startPos, 0)       # Add fruit collected at the start position.