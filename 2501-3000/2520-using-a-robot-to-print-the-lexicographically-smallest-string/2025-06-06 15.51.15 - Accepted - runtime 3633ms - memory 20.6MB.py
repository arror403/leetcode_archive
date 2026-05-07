
class Solution:
    def robotWithString(self, s: str) -> str:
        t, res = [], ""
        d = Counter(s)
        
        for c in s:
            t.append(c)
            d[c] -= 1
            min_char = min(char for char in d if d[char] > 0) if any(d.values()) else 'z'
            
            while t and t[-1] <= min_char:
                res += t.pop()
        
        
        return res + ''.join(reversed(t))