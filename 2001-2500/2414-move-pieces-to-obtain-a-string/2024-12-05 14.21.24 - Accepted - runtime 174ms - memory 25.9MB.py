class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove underscores and check if the non-underscore characters are the same
        p = ''.join([c for c in start if c != "_"])
        q = ''.join([c for c in target if c != "_"])
        if p != q: return False
        
        # Track indices of 'L' and 'R' in the start string
        d = defaultdict(list)
        for i, c in enumerate(start):
            d[c].append(i)
        
        # Check 'L' moves
        l_indices_start = d['L']
        l_indices_target = [i for i, c in enumerate(target) if c == 'L']
        
        for start_idx, target_idx in zip(l_indices_start, l_indices_target):
            # 'L' can only move left, so start index must be >= target index
            if start_idx < target_idx:
                return False
        
        # Check 'R' moves
        r_indices_start = d['R']
        r_indices_target = [i for i, c in enumerate(target) if c == 'R']
        
        for start_idx, target_idx in zip(r_indices_start, r_indices_target):
            # 'R' can only move right, so start index must be <= target index
            if start_idx > target_idx:
                return False
        
        
        return True