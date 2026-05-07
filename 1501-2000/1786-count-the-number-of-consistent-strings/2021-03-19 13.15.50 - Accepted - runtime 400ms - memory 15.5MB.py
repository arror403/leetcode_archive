class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        sum=0
  
        for i in allowed:
            for j in range(0,len(words)):
                words[j]=(words[j]).replace(i,'')
            
        for s in words:
            if s=='':
                sum+=1
                    
                    
        return sum
                