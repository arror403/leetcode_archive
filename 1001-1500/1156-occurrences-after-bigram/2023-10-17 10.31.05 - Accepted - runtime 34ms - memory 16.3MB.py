class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        # return [i for i,v in enumerate(text.split()) if ]
        text=text.split()
        text.reverse()
        l=len(text)
        res=[]
        for i,v in enumerate(text):
            # print(i,v)
            if i==(l-2): break
            
            if text[i+2]==first and text[i+1]==second: 
                res.append(v)

        return res