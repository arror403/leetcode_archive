class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        d = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        
        # Build prefix directly as tuples for set compatibility
        x = y = 0
        pre = [(0, 0)]
        for c in s:
            x += d[c][0]
            y += d[c][1]
            pre.append((x, y))
        
        # Collect distinct skip points
        return len({(pre[i][0]+x-pre[i+k][0], pre[i][1]+y-pre[i+k][1]) for i in range(len(s)-k+1)})