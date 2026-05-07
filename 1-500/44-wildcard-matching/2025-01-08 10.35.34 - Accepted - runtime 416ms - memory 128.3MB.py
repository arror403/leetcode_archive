class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def match(i: int, j: int) -> bool:
            # Base cases
            if j == len(p):  # Pattern is exhausted
                return i == len(s)  # String should also be exhausted
            
            # Current pattern character matches current string character
            first_match = i < len(s) and (p[j] == '?' or p[j] == s[i])
            
            if p[j] == '*':
                # Two choices with '*':
                # 1. '*' matches nothing (skip '*'): match(i, j+1)
                # 2. '*' matches current char and remains: match(i+1, j)
                return match(i, j+1) or (i < len(s) and match(i+1, j))
            else:
                # For '?' or exact match, both string and pattern must advance
                return first_match and match(i+1, j+1)
        
        return match(0, 0)