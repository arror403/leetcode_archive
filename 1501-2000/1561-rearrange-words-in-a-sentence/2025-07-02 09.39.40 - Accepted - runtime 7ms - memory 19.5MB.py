class Solution:
    def arrangeWords(self, text: str) -> str:
        s=text.split()
        s.sort(key=len)

        s[0]=s[0][0].upper()+s[0][1:]

        for i in range(1,len(s)): s[i]=s[i].lower()


        return ' '.join(s)