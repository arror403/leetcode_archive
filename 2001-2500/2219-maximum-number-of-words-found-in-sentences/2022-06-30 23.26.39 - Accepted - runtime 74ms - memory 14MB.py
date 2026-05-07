class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        b=[]
        for i in sentences:
            i=i.split()
            b.append(len(i))
            
        return (max(b))