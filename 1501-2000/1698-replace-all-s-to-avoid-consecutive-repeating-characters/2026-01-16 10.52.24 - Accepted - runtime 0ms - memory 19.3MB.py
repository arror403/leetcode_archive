class Solution:
    def modifyString(self, s: str) -> str:
        # We only need 3 characters ('a', 'b', 'c') to ensure no two adjacent characters are the same.
        L = len(s)
        s = list(s)

        for i in range(L):
            if s[i] == '?':
                # Create a set of "forbidden" characters based on neighbors
                forbidden = set()
                # left neighbor
                if i > 0:
                    forbidden.add(s[i-1])
                # right neighbor
                if i < L - 1:
                    forbidden.add(s[i+1])

                for c in 'abc':
                    if c not in forbidden:
                        s[i] = c
                        break
        
        
        return ''.join(s)