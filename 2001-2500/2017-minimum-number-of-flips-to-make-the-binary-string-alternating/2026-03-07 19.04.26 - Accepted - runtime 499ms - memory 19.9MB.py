class Solution:
    def minFlips(self, s: str) -> int:
        L = len(s)
        s = s + s  # double the string to simulate all rotations
        
        # Pattern 0: "010101..."
        # Pattern 1: "101010..."
        diff0 = 0  # mismatches with pattern "010101..." for current window
        diff1 = 0  # mismatches with pattern "101010..."
        
        res = L  # worst case
        
        for i in range(L*2):
            # For pattern 0: position i should be i % 2
            if int(s[i]) != i % 2:
                diff0 += 1
            # For pattern 1: position i should be (i + 1) % 2
            if int(s[i]) != (i + 1) % 2:
                diff1 += 1
            
            # Remove the element leaving the window (when window exceeds size L)
            if i >= L:
                j = i - L  # element to remove
                if int(s[j]) != j % 2:
                    diff0 -= 1
                if int(s[j]) != (j + 1) % 2:
                    diff1 -= 1
            
            # Once we have a full window of size L, update result
            if i >= L - 1:
                res = min(res, diff0, diff1)
        
        return res