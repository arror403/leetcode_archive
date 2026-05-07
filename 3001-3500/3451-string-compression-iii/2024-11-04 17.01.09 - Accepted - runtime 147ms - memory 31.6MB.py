class Solution:
    def compressedString(self, word: str) -> str:
        d=[list(g) for _,g in groupby(word)]
        res=""

        for e in d:
            q,r=divmod(len(e),9)
            res+=('9'+e[0])*q
            
            if r>0: res+=str(r)+e[0]


        return res