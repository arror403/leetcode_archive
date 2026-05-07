class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        r=''.join(c if c!="*" else ".*" for c in p)
        substrings=[s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]

        for x in substrings:
            m=re.search(r, x)
            if m:
                if m.group(0)==x:
                    return True


        return False