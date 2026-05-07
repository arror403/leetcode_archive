class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c1,c2,c3=True,True,False
        
        for i in word:
            if i.islower():
                continue
            else:
                c1=False
                break
                
        for i in word:
            if i.isupper():
                continue
            else:
                c2=False
                break
                
        if word[0].isupper():        
            for i in range(1,len(word)):
                if word[i].islower():
                    c3=True
                    continue
                else:
                    c3=False
                    break
                    
        return 1 if c1 or c2 or c3 else 0