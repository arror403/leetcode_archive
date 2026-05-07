class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        r=p.replace('*', '.*', 1)

        for x in [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]:
            m=re.search(r, x)
            if m and m.group(0)==x:
                return True


        return False