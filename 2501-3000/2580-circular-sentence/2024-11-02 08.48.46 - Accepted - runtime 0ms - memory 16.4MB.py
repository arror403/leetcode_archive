class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        m=sentence.split()
        m.append(m[0])
        
        for a,b in pairwise(m):
            if a[-1]!=b[0]: return False

        return True