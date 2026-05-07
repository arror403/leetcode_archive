class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        t=""
        for x in paragraph:
            if x in "!?',;.":
                t+=" "
            else:
                t+=x

        p=[c.lower() for c in t.split()]
        d=sorted(Counter(p).items(), key=lambda x:x[1], reverse=1)
        # print(d)
        for x in d:
            if x[0] not in banned:
                return x[0]

        return ''