class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['A','E','I','O','U','a','e','i','o','u']
        res=[]
        x=0

        p=[i for i,v in enumerate(s) if v in vowels]
        sorted_v=sorted([i for i in s if i in vowels])

        # print(p,tmp)

        for i,v in enumerate(s):
            if x<len(p) and i==p[x]:
                res.append(sorted_v[x])
                x+=1
            else:
                res.append(v)

        return ''.join(res)