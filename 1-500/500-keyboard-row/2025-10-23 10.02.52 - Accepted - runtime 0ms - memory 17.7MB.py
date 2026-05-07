class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set("qwertyuiopQWERTYUIOP")
        b = set("asdfghjklASDFGHJKL")
        c = set("zxcvbnmZXCVBNM")

        res = []
        for w in words:
            t = set(w)
            if t <= a:
                res.append(w)
            elif t <= b:
                res.append(w)
            elif t <= c:
                res.append(w)


        return res