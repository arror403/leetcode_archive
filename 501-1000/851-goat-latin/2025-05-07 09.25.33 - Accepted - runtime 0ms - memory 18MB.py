class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        i=1
        res=[]

        for s in sentence.split():
            if s[0] in "aeiouAEIOU":
                s+="ma"
            else:
                s=s[1:]+s[0]+"ma"
            
            s+="a"*i
            i+=1

            res.append(s)


        return ' '.join(res)