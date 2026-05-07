class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        b=[]
        for i in words:
            s=""
            for j in i:
                s+=morse[ord(j)-97]
            b.append(s)
        b = list(dict.fromkeys(b))
        return len(b)