class Solution:
    def reverseWords(self, s: str) -> str:
        t=s.split()
        c=len([x for x in t[0] if x in "aeiou"])
        res=[t[0]]

        for p in t[1:]:
            if len([x for x in p if x in "aeiou"])==c:
                res.append(p[::-1])
            else:
                res.append(p)


        return ' '.join(res)