class Solution:
    def generateTag(self, caption: str) -> str:
        s=caption.split()
        if not s: return '#'

        s=[c[0].upper()+''.join([x.lower() for x in c[1:]]) for c in s]

        s[0]=s[0][0].lower()+s[0][1:]
            
        s='#'+''.join(s)


        return s[:100]