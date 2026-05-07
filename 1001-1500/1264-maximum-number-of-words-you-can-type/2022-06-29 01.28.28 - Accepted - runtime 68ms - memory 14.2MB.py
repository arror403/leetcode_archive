class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        t=0
        text = text.split()
        brokenLetters=list(brokenLetters)
        b=[]
        for i in text:
            b.append(list(i))
            
        for i in b:
            f=0
            for j in brokenLetters:
                if (j in i):
                    f=1
                    break
                    
            if f==0:
                t+=1
                
        return t
                                        
                        
            
        