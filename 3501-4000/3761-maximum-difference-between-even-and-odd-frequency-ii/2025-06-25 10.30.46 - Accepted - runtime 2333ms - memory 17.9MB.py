class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(x, y): 
            return ((x&1)<<1)|(y&1)
        
        n = len(s)
        res = float('-inf')
        
        # Only iterate over characters that actually exist in the string
        unique_chars = list(set(s))
        
        for a in unique_chars:
            for b in unique_chars:
                if a == b: 
                    continue
                    
                best = [float('inf')] * 4
                cnt_a = cnt_b = prev_a = prev_b = 0
                left = 0
                
                for right in range(n):
                    # Count characters in current window
                    if s[right] == a:
                        cnt_a += 1
                    if s[right] == b:
                        cnt_b += 1
                    
                    # Shrink window while it's valid and has at least k elements
                    while (right - left + 1 >= k) and (cnt_b - prev_b >= 2):
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        
                        # Move left pointer and update prev counts
                        if s[left] == a:
                            prev_a += 1
                        if s[left] == b:
                            prev_b += 1
                        left += 1
                    
                    # Check if we can form a valid subarray
                    right_status = getStatus(cnt_a, cnt_b)
                    required_status = right_status ^ 2  # Flip the second bit
                    
                    if best[required_status] != float('inf'):
                        res = max(res, cnt_a - cnt_b - best[required_status])
        
        
        return res if res != float('-inf') else -1