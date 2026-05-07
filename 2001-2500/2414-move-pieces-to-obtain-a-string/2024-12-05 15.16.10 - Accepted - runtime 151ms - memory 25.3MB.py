class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if [c for c in start if c != "_"] != [c for c in target if c != "_"]: 
            return False
        
        d = defaultdict(list)
        for i, c in enumerate(start):
            d[c].append(i)

        li = [i for i, c in enumerate(target) if c == 'L']
        for start_idx, target_idx in zip(d['L'], li):
            # 'L' can only move left, so start index must be >= target index
            if start_idx < target_idx:
                return False

        ri = [i for i, c in enumerate(target) if c == 'R']
        for start_idx, target_idx in zip(d['R'], ri):
            # 'R' can only move right, so start index must be <= target index
            if start_idx > target_idx:
                return False
        

        return True