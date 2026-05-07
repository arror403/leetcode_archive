class Solution:
    def sortVowels(self, s: str) -> str:
        vowels={'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
        vi=[]
        vc=[]
        
        for i,c in enumerate(s):
            if c in vowels:
                vi.append(i)
                vc.append(c)

        vc.sort()

        res=list(s)
        t=0
        for x in vi:
            res[x]=vc[t]
            t+=1


        return ''.join(res)