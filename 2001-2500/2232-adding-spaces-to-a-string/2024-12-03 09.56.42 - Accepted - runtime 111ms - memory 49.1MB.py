class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        t = deque(spaces)
        res = ''
        for i, c in enumerate(s):
            if not t:
                res += s[i:] 
                break

            if i == t[0]:
                res += " " + c
                t.popleft()
            else:
                res += c

        return res