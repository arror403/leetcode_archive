class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res=0
            
        for i in text.split():
            f=1
            for j in brokenLetters:
                if j in i:
                    f=0
                    break
                    
            if f: res+=1
                

        return res