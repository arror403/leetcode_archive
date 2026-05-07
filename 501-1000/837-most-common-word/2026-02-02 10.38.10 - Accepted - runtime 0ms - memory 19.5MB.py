class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.lower().replace(","," ").replace("."," ").replace("!"," ").replace("?"," ").replace("/"," ").replace("'"," ").replace(";"," ").split() # weird, but works

        para_sorted = sorted(Counter(p).items(), key=lambda x:x[1], reverse=True)

        for k,v in para_sorted:
            if k not in banned:
                return k