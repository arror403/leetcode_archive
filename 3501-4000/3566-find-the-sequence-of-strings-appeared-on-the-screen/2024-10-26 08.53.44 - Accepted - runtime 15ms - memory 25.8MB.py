class Solution:
    def stringSequence(self, target: str) -> List[str]:
        res=[]
        tmp=""
        m=[ord(c)-97 for c in target]

        for i in m:
            for j in range(i+1):
                res.append(tmp+chr(j+97))
            tmp=res[-1]


        return res