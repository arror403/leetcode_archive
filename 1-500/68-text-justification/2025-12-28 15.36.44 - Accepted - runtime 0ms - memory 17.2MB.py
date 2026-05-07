class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        L=[len(w) for w in words]
        s=[]
        res=[]
        n=0

        for l, w in zip(L,words):
            if n+l+len(s) > maxWidth:
                if len(s)==1:
                    res.append(s[0] + ' '*(maxWidth-n))
                else:
                    a, b = divmod((maxWidth-n), len(s)-1)
                    for i in range(b):
                        s[i] += ' '
                    res.append((' '*a).join(s))

                s, n = [], 0

            s.append(w)
            n += l


        return res + [' '.join(s) + ' '*(maxWidth-n-len(s)+1)]