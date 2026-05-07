class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        
        # Compute prefix sums
        pre = [[0, 0]]
        for c in s:
            dx, dy = d[c]
            pre.append([pre[-1][0] + dx, pre[-1][1] + dy])
        
        # Instead of precomputing suffix, use the fact that:
        # suffix[i] = total - pre[i]
        total_x, total_y = pre[n]
        
        # Collect distinct points
        seen = set()
        for i in range(n - k + 1):
            # Position = pre[i] + (total - pre[i+k])
            x = pre[i][0] + total_x - pre[i + k][0]
            y = pre[i][1] + total_y - pre[i + k][1]
            seen.add((x, y))
        
        
        return len(seen)